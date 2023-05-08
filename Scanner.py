import tkinter as tk
from datetime import datetime
import json
import time
import data
import hashlib

Cabinet_Type=''
Cabinet_Customer=''
Cabinet=''
Serial_number=''
Spot_cabinet=''

win_size='800x600'

with open('Technitians.json','r+') as File_Technitians_list:
    Technitian_list=json.load(File_Technitians_list)
List_technitians_data=Technitian_list['Technitians']

#open json cabinets history
with open('Cabinets_History.json') as file_tracking_done:
    Cabinets_done=json.load(file_tracking_done)
list_cabinets_done=Cabinets_done['cabinets']

def Scanner_done(event, Scanner_index):
    i=0
    find=False

def write_json(new_data):
    with open('Tracking_Cabinets.json','r+') as fi:
        file_data=json.load(fi)
        #print('exists')
        #print(file_data)
        file_data['cabinets'].append(new_data)
        fi.seek(0)
        json.dump(file_data,fi,indent=4)
    #Open json tracking cabinets
    file_tracking=open('Tracking_Cabinets.json')
    Cabinets_in_production=json.load(file_tracking)
    list_cabinets_in_floor=Cabinets_in_production['cabinets']
    file_tracking.close()
    print(list_cabinets_in_floor)

def update_list_cabinets_in_floor():
    global list_cabinets_in_floor
    file_tracking=open('Tracking_Cabinets.json')
    Cabinets_in_production=json.load(file_tracking)
    list_cabinets_in_floor=Cabinets_in_production['cabinets']
    file_tracking.close()

def Place_Entry():
    Disp_Technitian_lbl.grid_forget()
    Disp_Spot_lbl.grid_forget()
    Disp_Cabinet_Type_lbl.grid_forget()
    Disp_Customer_lbl.grid_forget()
    Disp_Cabinet_PN_lbl.grid_forget()
    Disp_SN_lbl.grid_forget()
    Done_button.grid_forget()
    Data_done.grid_forget()

    Technitian_Entry.delete(0,'end')
    Technitian_Entry.grid(row=0,column=1,sticky='W')
    Spot_Entry.delete(0,'end')
    Spot_Entry.grid(row=1,column=1,sticky='W')
    Cabinet_Type_Entry.delete(0,'end')
    Cabinet_Type_Entry.grid(row=2,column=1,sticky='W')
    Customer_Entry.delete(0,'end')
    Customer_Entry.grid(row=3,column=1,sticky='W')
    Cabinet_PN_Entry.delete(0,'end')
    Cabinet_PN_Entry.grid(row=4,column=1,sticky='W')
    SN_Entry.delete(0,'end')
    SN_Entry.grid(row=5,column=1,sticky='W')
    Technitian_Entry.focus()
    
def Place_labels():
    global Label_technitian_value

    #Technitian
    Technitian_Entry.grid_forget()
    #Set value to Disp_Technitian_lbl
    Disp_Technitian_lbl.configure(text=Technitian_Entry.get())
    Disp_Technitian_lbl.grid(row=0,column=1,sticky='W')

    #Spot
    Spot_Entry.grid_forget()
    Disp_Spot_lbl.configure(text=Spot_Entry.get())
    Disp_Spot_lbl.grid(row=1,column=1,sticky='W')

    #Type
    Cabinet_Type_Entry.grid_forget()
    Disp_Cabinet_Type_lbl.configure(text=Cabinet_Type_Entry.get())
    Disp_Cabinet_Type_lbl.grid(row=2,column=1,sticky='W')

    #customer
    Customer_Entry.grid_forget()
    Disp_Customer_lbl.configure(text=Customer_Entry.get())
    Disp_Customer_lbl.grid(row=3,column=1,sticky='W')

    #Cabinet
    Cabinet_PN_Entry.grid_forget()
    Disp_Cabinet_PN_lbl.configure(text=Cabinet_PN_Entry.get())
    Disp_Cabinet_PN_lbl.grid(row=4,column=1,sticky='W')

    #Serial number
    SN_Entry.grid_forget()
    Disp_SN_lbl.configure(text=SN_Entry.get())
    Disp_SN_lbl.grid(row=5,column=1,sticky='W')

    #Done button
    Done_button.grid(row=6,column=0,sticky='W')

    Message_lbl.grid(row=7,column=0,columnspan=2)
    Message_lbl2.grid(row=8,column=0,columnspan=2)
             
    Message_lbl.configure(text="--Escanear credencial del Tecnico--")
    Message_lbl2.configure(text="--A new cabinet was recorded--")

#Process Done, this function is called when the cabinet is done
def Done_electrical_test(index):
    global list_cabinets_in_floor
    with open('Tracking_Cabinets.json','r+') as fi:
        Cabinets_data=json.load(fi)
        Cabinets_data['cabinets'][index]['Stamp_time_done']=str(datetime.now())
        fi.seek(0)
        json.dump(Cabinets_data,fi,indent=4)
    update_list_cabinets_in_floor()
    with open('Cabinets_History.json','r') as readCabinets_history:
        Cabinets_data_history=json.load(readCabinets_history)
        Cabinets_data_history['cabinets'].append(list_cabinets_in_floor[index])
    with open('Cabinets_History.json','w') as writeCabinets_history:
        json.dump(Cabinets_data_history,writeCabinets_history,indent=1)
    #Remove cabinet for the list of the floor production
    with open('Tracking_Cabinets.json','r') as readCabinets:
        print("delete")
        Cabinets_data=json.load(readCabinets)
        print(Cabinets_data['cabinets'][index])
        del Cabinets_data['cabinets'][index]
    with open('Tracking_Cabinets.json','w') as writeCabinets:
        json.dump(Cabinets_data,writeCabinets,indent=4)
    Message_lbl.configure(text="--Cabinet complete--")
    Message_lbl2.configure(text="--Scan new cabinet--")
    windows.geometry(win_size)
    Place_Entry()

    '''
    with open('Tracking_Cabinets.json','r+') as fi:
        Cabinets_data=json.load(fi)
        Cabinets_data['cabinets'][index]['Stamp_time_mechanical_assembly']=Cabinets_data['cabinets'][index]['Stamp_time']
        Cabinets_data['cabinets'][index]['Current_place']="Waiting electrical assembly"
        Cabinets_data['cabinets'][index]['Stamp_time']=str(datetime.now())
        Cabinets_data['cabinets'][index]['Technitian_Mechanical']=Cabinets_data['cabinets'][index]['Technitian']
        fi.seek(0)
        json.dump(Cabinets_data,fi,indent=4)
        list_cabinets_in_floor=Cabinets_data['cabinets']
    Message_lbl.configure(text="--Electrical test complete--")
    Message_lbl2.configure(text="--Now record a new cabinet--")
    #print(list_cabinets_in_floor)
    windows.geometry(win_size)
    Place_Entry()
    '''
    
def Done_electrical_assembly(index):
    with open('Tracking_Cabinets.json','r+') as fi:
        Cabinets_data=json.load(fi)
        Cabinets_data['cabinets'][index]['Stamp_time_electrical_assembly']=Cabinets_data['cabinets'][index]['Stamp_time']
        Cabinets_data['cabinets'][index]['Stamp_time']=str(datetime.now())
        Cabinets_data['cabinets'][index]['Technitian_Electrical_Assembly']=Cabinets_data['cabinets'][index]['Technitian']
        Cabinets_data['cabinets'][index]['Current_place']="Waiting electrical test"
        fi.seek(0)
        json.dump(Cabinets_data,fi,indent=4)
    Place_Entry()
    Message_lbl.configure(text="--Electrical assembly complete--")
    Message_lbl2.configure(text="--Now is waiting to electrical test--")
    windows.geometry(win_size)
    Done_button.pack_forget()

    #Done_electrical_test

def Done_mechanical_assembly(index):
    with open('Tracking_Cabinets.json','r+') as fi:
        Cabinets_data=json.load(fi)
        Cabinets_data['cabinets'][index]['Stamp_time_electrical_test']=Cabinets_data['cabinets'][index]['Stamp_time']
        Cabinets_data['cabinets'][index]['Stamp_time']=str(datetime.now())
        Cabinets_data['cabinets'][index]['Technitian_Electrical_Test']=Cabinets_data['cabinets'][index]['Technitian']
        Cabinets_data['cabinets'][index]['Current_place']="Waiting Packing"
        fi.seek(0)
        json.dump(Cabinets_data,fi,indent=4)
    Place_Entry()
    Message_lbl.configure(text="--Electrical test complete--")
    Message_lbl2.configure(text="--Now is waiting for Packing--")
    windows.geometry(win_size)
    Done_button.pack_forget()

        #Done_quality_inspection
def Done_quality_inspection(index):
    #Add cabinet to the lis of the history list
    print("Quality############################@%$^%$&^*&%(")
    print(list_cabinets_in_floor[index])
    with open('Cabinets_History.json','r') as readCabinets_history:
        Cabinets_data_history=json.load(readCabinets_history)
        Cabinets_data_history['cabinets'].append(list_cabinets_in_floor[index])
    with open('Cabinets_History.json','w') as writeCabinets_history:
        json.dump(Cabinets_data_history,writeCabinets_history,indent=1)
    #Remove cabinet for the list of the floor production
    with open('Tracking_Cabinets.json','r') as readCabinets:
        print("delete")
        Cabinets_data=json.load(readCabinets)
        print(Cabinets_data['cabinets'][index])
        del Cabinets_data['cabinets'][index]
    with open('Tracking_Cabinets.json','w') as writeCabinets:
        json.dump(Cabinets_data,writeCabinets,indent=4)
    Message_lbl.configure(text="--Cabinet complete--")
    Message_lbl2.configure(text="--Scan new cabinet--")
    windows.geometry(win_size)

        #Done_packing
def Done_packing(index):
    update_list_cabinets_in_floor()
    with open('Tracking_Cabinets.json','r') as readCabinets:
        Cabinets_data=json.load(readCabinets)    
        Cabinets_data['cabinets'][index]['Current_place']="Waiting Quality inspection"
        Cabinets_data['cabinets'][index]['Stamp_time_packing']=Cabinets_data['cabinets'][index]['Stamp_time']
        Cabinets_data['cabinets'][index]['Stamp_time']=str(datetime.now())
        Cabinets_data['cabinets'][index]['Technitian_Packing']=Cabinets_data['cabinets'][index]['Technitian']
    with open('Tracking_Cabinets.json','w') as writeCabinets:
        json.dump(Cabinets_data,writeCabinets,indent=4)
    Place_Entry()
    Message_lbl.configure(text="--Quality inspection complete--")
    Message_lbl2.configure(text="--Now is waiting for Quality inspection--")
    windows.geometry(win_size)
    Done_button.pack_forget()

#check cabinet function
def Check_cabinet(event):
    global Done_button
    print("Check cabinet")
    print(Customer_Entry.get())
    global i_cabinet
    global Technitian
    global Label_technitian_value
    #global list_cabinets_in_floor
    Technitian_Entry.focus()
    #print(Data_input_name.get())
    #print(data.Technitian_validate)
    #Open json tracking cabinets
    file_tracking=open('Tracking_Cabinets.json')
    Cabinets_in_production=json.load(file_tracking)
    list_cabinets_in_floor=Cabinets_in_production['cabinets']
    file_tracking.close()
    print(Customer_Entry.get())
    
    if(data.Technitian_validate==True):

        ##Get data from the widgets##
        Technitian=Technitian_Entry.get()
        Cabinet_Type=Cabinet_Type_Entry.get()
        Cabinet_Customer=Customer_Entry.get()
        Cabinet=Cabinet_PN_Entry.get()
        Serial_number=SN_Entry.get()
        Cabinet_split=Cabinet.split()
        order=Cabinet_split[0]
        PartNumber=Cabinet_split[1]
        Spot=Spot_Entry.get()
        ##Get Checksum##
        Cabinet_header=Cabinet_Type+Cabinet_Customer+order+PartNumber+Serial_number
        Cabinet_MD5=hashlib.md5(Cabinet_header.encode())
        print('technitian index: '+str(technitian_index))

        #--------------------check if cabinet is on production---------------------#
        #--------------------------------------------------------------------------#
        #--------------------------------------------------------------------------#
        i_cabinet=0
        index_find=False
        while(i_cabinet<len(list_cabinets_in_floor) and index_find==False):    
            #print("i_cabinet= "+str(i_cabinet))
            #print("MD5: "+str(list_cabinets_in_floor[i_cabinet]['Checksum']))
            if(Cabinet_MD5.hexdigest()==list_cabinets_in_floor[i_cabinet]['Checksum']):
                index_find=True
            else:
                i_cabinet=i_cabinet+1
        print("i_cabinet: ",i_cabinet)
        print("lenght: ",len(list_cabinets_in_floor))
        print("checksum cabinet",Cabinet_MD5.hexdigest())
        try:
            print("checksum index",list_cabinets_in_floor[i_cabinet]['Checksum'])
        except:
            print("out of index")
        #print(list_cabinets_in_floor)


        #-------------Cabinet is in production-------------------#
                    #-------------------------------#
        if(i_cabinet<len(list_cabinets_in_floor)):
            if(Cabinet_MD5.hexdigest()==list_cabinets_in_floor[i_cabinet]['Checksum']):
                print('cabinet is in production line')
                        
            #mechanical assembly scan cabinet
                if(list_cabinets_in_floor[i_cabinet]['Current_place']=='Mechanical assembly'):
                    if(List_technitians_data[technitian_index]["process"]=="Mechanical assembly"):
                        windows.geometry(win_size)
                        #Button for check done
                        Done_button.bind('<Button-1>',Done_mechanical_assembly(i_cabinet))
                        Done_button.grid(row=5,column=0)
                        #Done_button = tk.Button(Frame_button,text="Done",width='10',command=lambda: Done_mechanical_assembly(i_cabinet))
                        #Done_button.pack(padx=10,side='left')
                        Place_labels()
                        Message_lbl.configure(text="--Current place: Mechanical assembly--")
                        Message_lbl2.configure(text="--In process--")
                    else:
                        Technitian_Entry.delete(0,'end')
                        Spot_Entry.delete(0,'end')
                        Customer_Entry.delete(0,'end')
                        Cabinet_Type_Entry.delete(0,'end')
                        SN_Entry.delete(0,'end')
                        Cabinet_PN_Entry.delete(0,'end')
                        Message_lbl.configure(text="--Current place: Mechanical assembly--")
                        Message_lbl2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")

            
                #Waiting electrical assembly
                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Waiting electrical assembly'):
                    if(List_technitians_data[technitian_index]["process"]=="Electrical assembly"):
                        print("Enter electrical assembly in waiting electrical assembly")
                        with open('Tracking_Cabinets.json','r') as readCabinets:
                            Cabinets_data=json.load(readCabinets)
                            Cabinets_data['cabinets'][i_cabinet]['Technitian_Mechanical']=Cabinets_data['cabinets'][i_cabinet]['Technitian']
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_time_Waiting_electrical_assembly']=Cabinets_data['cabinets'][i_cabinet]['Stamp_time']
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_time']=str(datetime.now())
                            Cabinets_data['cabinets'][i_cabinet]['Technitian']=Technitian_Entry.get()
                            Cabinets_data['cabinets'][i_cabinet]['Current_place']="Electrical assembly"
                        with open('Tracking_Cabinets.json','w') as writeCabinets: 
                            json.dump(Cabinets_data,writeCabinets,indent=4)
                        list_cabinets_in_floor=Cabinets_data['cabinets']
                        Done_button = tk.Button(Displaying_cabinet_data,text="Done",width='10',command=lambda: Done_electrical_assembly(i_cabinet))
                        Done_button.grid(row=5,column=0)
                        windows.geometry(win_size)
                        #Label_message.configure(text="--Current place: Electrical assembly--")
                        #Label_message_2.configure(text="--"+List_technitians_data[technitian_index]["process"]+"--")
                        #print(list_cabinets_in_floor)
                        Place_labels()
                        Label_technitian_value=tk.Label(Displaying_cabinet_data,font=("arial",16),text=List_technitians_data[technitian_index]["id"])
                        Label_technitian_value.pack(side='left',fill=tk.X,padx=10)
                        
                        
                    else:
                        Technitian_Entry.delete(0,'end')
                        Customer_Entry.delete(0,'end')
                        Cabinet_Type_Entry.delete(0,'end')
                        SN_Entry.delete(0,'end')
                        Spot_Entry.delete(0,'end')
                        Cabinet_PN_Entry.delete(0,'end')
                        Message_lbl.configure(text="--Waiting Electrical assembly--")
                        Message_lbl2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")
                

            #Electrical assembly
                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Electrical assembly'):
                    if(List_technitians_data[technitian_index]["process"]=="Electrical assembly"):
                        windows.geometry(win_size)
                        Done_button = tk.Button(text="Done",width='10',command=lambda: Done_electrical_assembly(i_cabinet))
                        Done_button.place(x=50, y=360)
                        Place_labels()
                        Message_lbl.configure(text="--Current place: Electrical assembly--")
                        Message_lbl2.configure(text="--In process--")
                    else:
                        Technitian_Entry.delete(0,'end')
                        Spot_Entry.delete(0,'end')
                        Customer_Entry.delete(0,'end')
                        Cabinet_Type_Entry.delete(0,'end')
                        SN_Entry.delete(0,'end')
                        Message_lbl.configure(text="--Current place: Electrical assembly--")
                        Message_lbl2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")


            #Waiting electrical test
                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Waiting electrical test'):
                    if(List_technitians_data[technitian_index]["process"]=="Electrical test"):
                        print("Enter electrical test in waiting electrical test")
                        with open('Tracking_Cabinets.json','r') as readCabinets:
                            Cabinets_data=json.load(readCabinets)    
                            Cabinets_data['cabinets'][i_cabinet]['Current_place']="Electrical test"
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_time_Waiting_electrical_test']=Cabinets_data['cabinets'][i_cabinet]['Stamp_time']
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_time']=str(datetime.now())
                            Cabinets_data['cabinets'][i_cabinet]['Technitian']=Technitian_Entry.get()
                        with open('Tracking_Cabinets.json','w') as writeCabinets:
                            json.dump(Cabinets_data,writeCabinets,indent=4)
                        list_cabinets_in_floor=Cabinets_data['cabinets']
                        Done_button = tk.Button(Displaying_cabinet_data,text="Done",width='10',command=lambda: Done_electrical_test(i_cabinet))
                        Done_button.place(x=50, y=360)
                        windows.geometry(win_size)
                        Place_labels()
                        #Label_message.configure(text="--Current place: Electrical assembly--")
                        #Label_message_2.configure(text="--"+List_technitians_data[technitian_index]["process"]+"--")
                        #print(list_cabinets_in_floor)
                        Technitian_Entry.delete(0,'end')
                        Spot_Entry.delete(0,'end')
                        Customer_Entry.delete(0,'end')
                        Cabinet_Type_Entry.delete(0,'end')
                        SN_Entry.delete(0,'end')
                    else:
                        Technitian_Entry.delete(0,'end')
                        Spot_Entry.delete(0,'end')
                        Customer_Entry.delete(0,'end')
                        Cabinet_Type_Entry.delete(0,'end')
                        SN_Entry.delete(0,'end')
                        Cabinet_PN_Entry.delete(0,'end')
                        Message_lbl.configure(text="--Waiting Electrical test--")
                        Message_lbl2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")

            #Electrical Test
            
                    
                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Electrical test'):
                    if(List_technitians_data[technitian_index]["process"]=="Electrical test"):
                        windows.geometry(win_size)
                        Place_labels()
                        Done_button.bind('<Button-1>',lambda event: Done_electrical_test(i_cabinet))
                        Message_lbl.configure(text="--Current place: Electrical test--")
                        Message_lbl2.configure(text="--In process--")
                        
                    else:
                        Technitian_Entry.delete(0,'end')
                        Spot_Entry.delete(0,'end')
                        Customer_Entry.delete(0,'end')
                        Cabinet_Type_Entry.delete(0,'end')
                        SN_Entry.delete(0,'end')
                        Message_lbl.configure(text="--Current place: Electrical test--")
                        Message_lbl2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")
                    
                
            #Waiting Quality inspection
                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Waiting Quality inspection'):
                    if(List_technitians_data[technitian_index]["process"]=="Quality inspection"):
                        print("Enter Quality inspector in waiting quality inspection")
                        with open('Tracking_Cabinets.json','r') as readCabinets:
                            Cabinets_data=json.load(readCabinets)    
                            Cabinets_data['cabinets'][i_cabinet]['Current_place']="Quality inspection"
                            Cabinets_data['cabinets'][i_cabinet]['Technitian_electrical_test']=Cabinets_data['cabinets'][i_cabinet]['Technitian']
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_time_Waiting_electrical_test']=Cabinets_data['cabinets'][i_cabinet]['Stamp_time']
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_time']=str(datetime.now())
                            Cabinets_data['cabinets'][i_cabinet]['Technitian']=Technitian_Entry.get()
                        with open('Tracking_Cabinets.json','w') as writeCabinets:
                            json.dump(Cabinets_data,writeCabinets,indent=4)
                        list_cabinets_in_floor=Cabinets_data['cabinets']
                        Done_button.bind('<Button-1>',Done_quality_inspection(i_cabinet))
                        Done_button.place(x=50, y=360)
                        windows.geometry(win_size)
                        Place_labels()
                        #Label_message.configure(text="--Current place: Electrical assembly--")
                        #Label_message_2.configure(text="--"+List_technitians_data[technitian_index]["process"]+"--")
                        #print(list_cabinets_in_floor)
                        Technitian_Entry.delete(0,'end')
                        Spot_Entry.delete(0,'end')
                        Customer_Entry.delete(0,'end')
                        Cabinet_Type_Entry.delete(0,'end')
                        SN_Entry.delete(0,'end')
                    else:
                        Technitian_Entry.delete(0,'end')
                        Spot_Entry.delete(0,'end')
                        Customer_Entry.delete(0,'end')
                        Cabinet_Type_Entry.delete(0,'end')
                        SN_Entry.delete(0,'end')
                        Message_lbl.configure(text="--Waiting Quality inspection--")
                        Message_lbl2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")

            #Quality

                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Quality inspection'):
                    if(List_technitians_data[technitian_index]["process"]=="Quality inspection"):
                        Done_button.bind('<Button-1>',lambda event: Done_quality_inspection(i_cabinet))
                        Done_button.place(x=50, y=360)
                        windows.geometry(win_size)
                        Place_labels()
                        Message_lbl.configure(text="--Current place: Quality inspection--")
                        Message_lbl2.configure(text="--In process--")
                    else:
                        Technitian_Entry.delete(0,'end')
                        Spot_Entry.delete(0,'end')
                        Customer_Entry.delete(0,'end')
                        Cabinet_Type_Entry.delete(0,'end')
                        SN_Entry.delete(0,'end')
                        Message_lbl.configure(text="--Current place: Quality inspection--")
                        Message_lbl2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")

            #Waiting Packing
                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Waiting Packing'):
                    if(List_technitians_data[technitian_index]["process"]=="Packing"):
                        print("Enter Quality inspector in waiting quality inspection")
                        with open('Tracking_Cabinets.json','r') as readCabinets:
                            Cabinets_data=json.load(readCabinets)    
                            Cabinets_data['cabinets'][i_cabinet]['Current_place']="Packing"
                            Cabinets_data['cabinets'][i_cabinet]['Technitian_Packing']=Cabinets_data['cabinets'][i_cabinet]['Technitian']
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_Waiting_packing']=Cabinets_data['cabinets'][i_cabinet]['Stamp_time']
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_time']=str(datetime.now())
                            Cabinets_data['cabinets'][i_cabinet]['Technitian']=Technitian_Entry.get()
                        with open('Tracking_Cabinets.json','w') as writeCabinets:
                            json.dump(Cabinets_data,writeCabinets,indent=4)
                        list_cabinets_in_floor=Cabinets_data['cabinets']
                        Done_button.bind('Button-1',lambda event: Done_packing(i_cabinet))
                        Done_button.place(x=50, y=360)
                        windows.geometry(win_size)
                        Place_labels()
                        #Label_message.configure(text="--Current place: Electrical assembly--")
                        #Label_message_2.configure(text="--"+List_technitians_data[technitian_index]["process"]+"--")
                        #print(list_cabinets_in_floor)
                        Technitian_Entry.delete(0,'end')
                        Spot_Entry.delete(0,'end')
                        Customer_Entry.delete(0,'end')
                        Cabinet_Type_Entry.delete(0,'end')
                        SN_Entry.delete(0,'end')
                        Cabinet_PN_Entry.delete(0,'end')
                    else:
                        Technitian_Entry.delete(0,'end')
                        Spot_Entry.delete(0,'end')
                        Customer_Entry.delete(0,'end')
                        Cabinet_Type_Entry.delete(0,'end')
                        SN_Entry.delete(0,'end')
                        Message_lbl.configure(text="--Waiting Packing--")
                        Message_lbl2.configure(text=List_technitians_data[technitian_index]["process"]+" access denied.")

            #Packing

                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Packing'):
                    if(List_technitians_data[technitian_index]["process"]=="Packing"):
                        Done_button.bind('Button-1',lambda event: Done_packing(i_cabinet))
                        Done_button.place(x=50, y=360)
                        windows.geometry(win_size)
                        Place_labels()
                        Message_lbl.configure(text="--Current place: Packing--")
                        Message_lbl2.configure(text="--In process--")
                    else:
                        Technitian_Entry.delete(0,'end')
                        Spot_Entry.delete(0,'end')
                        Customer_Entry.delete(0,'end')
                        Cabinet_Type_Entry.delete(0,'end')
                        SN_Entry.delete(0,'end')
                        Message_lbl.configure(text="--Current place: Packing--")
                        Message_lbl2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")

        ##Write Cabinet info to Json##
        #jsonString=json.dumps(Cabinet_info)
        #jsonFile=open("Tracking_Cabinets.json","w")
        #jsonFile.write(jsonString)
        #jsonFile.close()
        #with open("Tracking_Cabinets.json","w") as write_file:
         #   json.dump(Cabinet_info,write_file)
        #print(Cabinet_info)
        
                
                #Cabinet is not in production, now will be check if is in History
         #------------------------------------------------------------------------------------#
        #open json cabinets history
        
        elif(i_cabinet==len(list_cabinets_in_floor)):
            with open('Cabinets_History.json') as file_tracking_done:
                Cabinets_done=json.load(file_tracking_done)
            list_cabinets_done=Cabinets_done['cabinets']
            print(str(i_cabinet)+" "+str(len(list_cabinets_in_floor)))
            i_cabinet_done=0
            #looking up for the cabinet in the history file json
            while(i_cabinet_done<len(list_cabinets_done) and Cabinet_MD5.hexdigest()!=list_cabinets_done[i_cabinet_done]['Checksum']):
                #print(list_cabinets_done[i_cabinet_done]['Checksum'])
                i_cabinet_done=i_cabinet_done+1
            print("i_cabinet_done: "+str(i_cabinet_done))

            #Cabinet is in History file
            if(i_cabinet_done<len(list_cabinets_done)):
                if(Cabinet_MD5.hexdigest()==list_cabinets_done[i_cabinet_done]['Checksum']):
                    Technitian_Entry.delete(0,'end')
                    Spot_Entry.delete(0,'end')
                    Customer_Entry.delete(0,'end')
                    Cabinet_Type_Entry.delete(0,'end')
                    SN_Entry.delete(0,'end')
                    data.Technitian_validate=False
                    Message_lbl.configure(text="--Cabinet is in History file--")
                    Message_lbl2.configure(text="--Finished cabinet--")

             #Cabinet doesn't exist, recording new cabinet
            elif(i_cabinet_done==len(list_cabinets_done) and i_cabinet==len(list_cabinets_in_floor)):
                if(List_technitians_data[technitian_index]["process"]=="Electrical test"):
                    Cabinet_info={"Technitian":Technitian_Entry.get(),"Checksum":Cabinet_MD5.hexdigest(),"Cabinet_type":Cabinet_Type,"Spot":Spot,"Customer":Cabinet_Customer,"Sales Order":order,"Cabinet_Part_Number":PartNumber,"Cabinet_SN":Serial_number,"Stamp_time":str(datetime.now()),"Current_place":"Electrical test"}
                    write_json(Cabinet_info)
                    windows.geometry(win_size)
                    Done_button.bind('<Button-1>',lambda event: Done_electrical_test(i_cabinet))
                    Done_button.grid(row=5,column=0)
                    Data_done.grid(row=6,column=0)
                    Data_done.focus()
                    

                    #Frame_technitian=tk.Frame(windows,width=200,height=50)
                    #Frame_technitian.pack(fill=tk.BOTH,expand=True)
                    #Label_technitian_value=tk.Label(Frame_technitian,font=("arial",16),text="Technician:")

                    Place_labels()

                    data.Technitian_validate=False
                    

                #Cabinet doesn't exist, The technitian is diferent to a mechanical assembly, can't record a new cabinet.
                elif(List_technitians_data[technitian_index]["process"]!="Mechanical assembly"):
                    Technitian_Entry.delete(0,'end')
                    Spot_Entry.delete(0,'end')
                    Customer_Entry.delete(0,'end')
                    Cabinet_Type_Entry.delete(0,'end')
                    SN_Entry.delete(0,'end')
                    Cabinet_PN_Entry.delete(0,'end')
                    data.Technitian_validate=False
                    Message_lbl.configure(text="--Technitian is not Mechanical assembly--")
                    Message_lbl2.configure(text="--Can't record new cabinet--")


#Check Technitians
def CheckandMove(event):
    global technitian_index
    start_time=time.time()
    end_time=0
    lapsed_time=0
    #data.Technitian_validate=True
    try:
        i=0
        find=False
        while(i<len(List_technitians_data) and find==False):
            if List_technitians_data[i]["id"]==Technitian_Entry.get():
                find=True
                technitian_index=i
                Spot_Entry.focus()
                dt = datetime.now()
                data.Technitian_validate=True
                Message_lbl2.configure(text="--Escanear Gabinete--")
                Message_lbl.configure(text=List_technitians_data[technitian_index]["firstName"]+" " +List_technitians_data[technitian_index]["lastName"]+" : "+List_technitians_data[technitian_index]["process"])
                Message_lbl.configure(bg="gold")
                Message_lbl2.configure(bg="gold")
                #Validate_technitian=Technitian_id.index(Data_input.get())
            i=i+1
        if find==False:
            windows.configure(bg="firebrick1")
            Record_cabinet_data.pack() 
            Technitian_Entry.delete(0,'end')
            Spot_Entry.delete(0,'end')
            Technitian_Entry.focus()
            Message_lbl.configure(text="--Tecnico no registrado--")
            Message_lbl2.configure(text="No found")
    except:
        windows.configure(bg="firebrick1")
        Record_cabinet_data.pack()
        #print(-1) 
        Technitian_Entry.delete(0,'end')
        Spot_Entry.delete(0,'end')
        Technitian_Entry.focus()
        Message_lbl.configure(text="--Tecnico no registrado--")
        Message_lbl2.configure(text="Error")
  
#Check Spot
def Spot(event):
    global Spot_cabinet
    Spot_value=Spot_Entry.get()
    #Spot_cabinet=Data_Spot.get()
    Cabinet_Type_Entry.focus()

def focusToCustomer(event):
    Customer_Entry.focus()

def focusToPN(event):
    Cabinet_PN_Entry.focus()

def focusToSN(event):
    SN_Entry.focus()

#windows GUI
windows=tk.Tk()
windows.geometry(win_size)
windows.title('Trafficware - Cabinets')
#windows.iconbitmap('Trafficlight.ico')

#Functions for User interface frame


###########################################################################
#---------------------------User interface frame--------------------------#
###########################################################################
Record_cabinet_data=tk.Frame(master=windows)

#Technitian
Technitian_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='Technitian: ',pady=10,justify='left')
Technitian_lbl.grid(row=0,column=0,sticky='W')
Technitian_Entry=tk.Entry(master=Record_cabinet_data,font=("arial",30))
Technitian_Entry.grid(row=0,column=1)
Technitian_Entry.bind('<Return>',CheckandMove)
Technitian_Entry.focus()

#Spot
Spot_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='Spot: ',pady=10,justify='left')
Spot_lbl.grid(row=1,column=0,sticky='W')
Spot_Entry=tk.Entry(master=Record_cabinet_data,font=("arial",30))
Spot_Entry.grid(row=1,column=1,)
Spot_Entry.bind('<Return>',Spot)

#Cabinet type
Cabinet_Type_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='Cabinet Type: ',pady=10)
Cabinet_Type_lbl.grid(row=2,column=0,sticky='W')
Cabinet_Type_Entry=tk.Entry(master=Record_cabinet_data,font=("arial",30))
Cabinet_Type_Entry.grid(row=2,column=1)
Cabinet_Type_Entry.bind('<Return>',focusToCustomer)

#Customer
Customer_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='Customer: ',pady=10)
Customer_lbl.grid(row=3,column=0,sticky='W')
Customer_Entry=tk.Entry(master=Record_cabinet_data,font=("arial",30))
Customer_Entry.grid(row=3,column=1)
Customer_Entry.bind('<Return>',focusToPN)

#Cabinet PN
Cabinet_PN_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='Cabinet PN: ',pady=10)
Cabinet_PN_lbl.grid(row=4,column=0,sticky='W')
Cabinet_PN_Entry=tk.Entry(master=Record_cabinet_data,font=("arial",30))
Cabinet_PN_Entry.grid(row=4,column=1)
Cabinet_PN_Entry.bind('<Return>',focusToSN)

#Serial Number
SN_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='SN: ',pady=10)
SN_lbl.grid(row=5,column=0,sticky='W')
SN_Entry=tk.Entry(master=Record_cabinet_data,font=("arial",30))
SN_Entry.grid(row=5,column=1)
SN_Entry.bind('<Return>',Check_cabinet)

#Message
Message_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='--Escanear credencial del Tecnico--',pady=10)

#Message 2
Message_lbl2=tk.Label(master=Record_cabinet_data,font=("arial",30),text='',pady=10)

Record_cabinet_data.pack()
Message_lbl.grid(row=7,column=0,columnspan=2)
Message_lbl2.grid(row=8,column=0,columnspan=2)

###########################################################################
#---------------------------Showing Data--------------------------#
###########################################################################
Displaying_cabinet_data=tk.Frame(master=windows)

#Technitian
Disp_Technitian_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='',pady=10,justify='left')

#Spot
Disp_Spot_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='',pady=10,justify='left')

#Cabinet type
Disp_Cabinet_Type_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='',pady=10)

#Customer
Disp_Customer_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='',pady=10)

#Cabinet PN
Disp_Cabinet_PN_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='',pady=10)

#Serial Number
Disp_SN_lbl=tk.Label(master=Record_cabinet_data,font=("arial",30),text='',pady=10)


#Button for check done
Done_button = tk.Button(master=Record_cabinet_data,text="Done",width='10')
Done_button.bind('<Button-1>',lambda event: Scanner_done(event, Scanner_index=i_cabinet))


#Data done - when the technitian scan the credential in Data_done
Data_done=tk.Entry(master=Record_cabinet_data,font=("arial",16))
Data_done.bind('<Return>',lambda event: Scanner_done(event, Scanner_index=i_cabinet))


windows.mainloop()   
