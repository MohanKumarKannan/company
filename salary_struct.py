# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 11:38:57 2018

@author: User
"""
allowance_threshold = 20000
derived_percent_config = .8
input_tctc = 1900000

class salary_struc:
    def __init__(self,salary):
        self.salary = salary

    def calc_total_salary(derived_ctc):    
        pa ={}
        derived_ctc = round(derived_ctc,0)
        pa['basic_pay'] = round((0.5 * derived_ctc),0)
        pm_basic_pay =round((pa['basic_pay']/12),0)
        pa['hra'] = round((0.5 * pa['basic_pay']),0)
        pa_allowance_incrementer = (pa['basic_pay']+pa['hra'])
        pa['conveyance_allowance']  = min(allowance_threshold, (derived_ctc-pa_allowance_incrementer))
        pa_allowance_incrementer+=pa['conveyance_allowance'] 
        pa['medical_reimbursement'] = min(allowance_threshold, (derived_ctc-pa_allowance_incrementer))
        pa_allowance_incrementer+=pa['medical_reimbursement']
        pa['lta'] =min(pm_basic_pay, derived_ctc-pa_allowance_incrementer)
        pa_allowance_incrementer+=pa['lta']
        pa['special_allowance'] = derived_ctc -(pa_allowance_incrementer)    
        pa['base_salary'] =pa_allowance_incrementer+pa['special_allowance']
           
        
        pa['employee_pf'] = 21600
        pa['gratuity'] = round((.0481*pa['basic_pay']),0)
        pa['mediclaim'] =21000
        pa['life_insurance'] = 700
        pa['benefits'] = (pa['employee_pf']+pa['gratuity']+pa['mediclaim']+pa['life_insurance'])
        tctc = pa['base_salary'] +pa['benefits']
    
        return pa,tctc
        
    
    
    def do_process(salary):
        derived_tctc = (derived_percent_config* salary)
        derived_ctc= 0
        while derived_tctc < (salary-0.5):
            derived_ctc += (salary - derived_tctc)/2    
            pa,derived_tctc =(salary_struc.calc_total_salary(derived_ctc))
            #print(derived_ctc,derived_tctc)
        return round(derived_ctc,0),derived_tctc,pa
    
    def print_struc(salary):
        derived_ctc,derived_tctc,pa= salary_struc.do_process(salary)
        print("                              COMPENSATION STRUCTURE      ")
        print ("FIXED COMPONENT        ,   PM            ,   PA    ") 
        print("Basic Pay              , INR  %s" % str(int(round(pa['basic_pay']/12,0))) , ",  INR " , int(pa['basic_pay']) )
        print("House Rent Allowance   , INR  %s" % str(int(round(pa['hra']/12,0))) , ",  INR " , int(pa['hra']) )       
        print("Conveyance Allowance   , INR  %s" % str(int(round(pa['conveyance_allowance']/12,0))) , ",  INR " , int(pa['conveyance_allowance']) )     
        print("Medical Reimbursement  , INR  %s" % str(int(round(pa['medical_reimbursement']/12,0))) , ",  INR " , int(pa['medical_reimbursement']) )               
        print("LTA                    , INR  %s" % str(int(round(pa['lta']/12,0))) , ",  INR " , int(pa['lta']) )             
        print("Special Allowance      , INR  %s" % str(int(round(pa['employee_pf']/12,0))) , ",  INR " , int(pa['employee_pf']) )            
        print("Total Base Salary [A]  , INR  %s" % str(int(round(pa['base_salary']/12,0))) , ",  INR " , int(pa['base_salary']) )          
        print("BENEFITS "  )          
        print("Employer PF           , INR  %s" % str(int(round(pa['employee_pf']/12,0))) , ",  INR " , int(pa['employee_pf']) )
        print("Gratuity              , INR  %s" % str(int(round(pa['gratuity']/12,0))) , ",  INR " , int(pa['gratuity']) )
        print("Mediclaim             , INR  %s" % str(int(round(pa['mediclaim']/12,0))) , ",  INR " , int(pa['mediclaim']) )        
        print("Life Insurance        , INR  %s" % str(int(round(pa['life_insurance']/12,0))) , ",  INR " , int(pa['life_insurance']) ) 
        print("Total Benefits [B]    , INR  %s" % str(int(round(pa['benefits']/12,0))) ,  ",  INR " , int(pa['benefits']) )                          
        print("Total CTC [A+B]       , INR  %s" % str(int(round(salary/12,0))) ,      ",  INR " , salary )    
        return derived_ctc,derived_tctc                     
                  
        


if __name__ =="__main__":
    l = [1250000,1200000,2200000,1300000,1550000]
    for i in l:
        derived_ctc, derived_tctc = salary_struc.print_struc(i)
        print('-----------------------------------------------------------------------------')        
        print(derived_ctc,derived_tctc)
        print('-----------------------------------------------------------------------------')

        
