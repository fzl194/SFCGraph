---
id: UDG@20.15.2@MMLCommand@DSP LICENSE
type: MMLCommand
name: DSP LICENSE（显示License）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LICENSE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# DSP LICENSE（显示License）

## 功能

该命令用于请求License文件状态信息、控制项信息以及销售项信息。

> **说明**
> - 当系统中不存在激活的License时，激活License文件、产品名称、产品版本等信息，显示为“NULL”。
> - 查询“销售项信息”时，如果销售项在授权截止日期内，则正常显示；如果销售项超过授权截止日期，则不显示。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSPBBOM | 显示类型 | 可选必选说明：可选参数。<br>参数含义：用于指示系统需要按照哪种类型来显示对应的信息。<br>取值范围：<br>- “CONTROLITEM(控制项信息)”：表示查询控制项的信息。<br>- “SALESITEM(销售项信息)”：表示查询销售项的信息。- 2.0版本的License文件无销售项信息，不支持显示销售项信息。<br>- 3.0版本的License文件是否显示销售项信息，由网元自定义控制。<br>- 该参数中国区暂不支持。<br>默认值：“CONTROLITEM(控制项信息)”。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LICENSE]] · 失效License（LICENSE）

## 使用实例

查询当前使用的2.0版本License文件状态信息以及控制项信息：

```
%%DSP LICENSE: DSPBBOM=CONTROLITEM;%%
RETCODE = 0  操作成功

当前License信息
---------------
         当前状态  =  进入宽限期
已激活License文件  =  LICENSANXXXXXXX.dat
         激活时间  =  2019-01-05 19:40:40
       设备序列号  =  7CDB4A586DD857F226XXXXXXXXX
             版本  =  2.0
       宽限期详情  =  共计60天，剩余39天
       试用期详情  =  NULL
    License失效码  =  LIC201711160XXXXX:66326438736BC7FBCC0C15D9BDBA14XXXXXXX
         失效时间  =  2019-10-05 09:43:24              
     启动紧急详情  =  上限3次，剩余2次                 
           序列号  =  LIC201602294XXXXX
         生成时间  =  2016-01-05 09:43:24
         产品名称  =  vXXXXX
         产品版本  =  V10XXXXXX
           顺序号  =  1
(结果个数 = 1)

控制项信息
----------
控制项         控制项描述                             当前授权值            授权截止日期  
                     
KV3S034FQP00   XX基本软件                             1000                  2024-12-30                                        
(结果个数 = 1)

---    END
```

查询当前使用的2.0版本License文件状态信息以及销售项信息：

```
%%DSP LICENSE: DSPBBOM=SALESITEM;%%
RETCODE = 0  操作成功

当前License信息
---------------
         当前状态  =  进入宽限期
已激活License文件  =  LICENSANXXXXXXX.dat
         激活时间  =  2019-01-05 19:40:40
       设备序列号  =  7CDB4A586DD857F226XXXXXXXXX
             版本  =  2.0
       宽限期详情  =  共计60天，剩余39天
       试用期详情  =  NULL
    License失效码  =  LIC201711160XXXXX:66326438736BC7FBCC0C15D9BDBA14XXXXXXX
         失效时间  =  2019-10-05 09:43:24              
     启动紧急详情  =  上限3次，剩余2次                 
           序列号  =  LIC201602294XXXXX
         生成时间  =  2016-01-05 09:43:24
         产品名称  =  vXXXXX
         产品版本  =  V10XXXXXX
           顺序号  =  1
(结果个数 = 1)

---    END
```

查询当前使用的3.0版本License文件状态信息以及控制项信息：

```
%%DSP LICENSE: DSPBBOM=CONTROLITEM;%%
RETCODE = 0  操作成功

当前License信息 
---------------          
         当前状态  =  进入宽限期 
已激活License文件  =  license_c20_XXXXXXXXX.xml          
         激活时间  =  2019-11-22 14:22:00        
       设备序列号  =  7CDB4A586DD857F226XXXXXXXXX              
             版本  =  3.0        
       宽限期详情  =  共计60天，剩余57天        
       试用期详情  =  NULL     
    License失效码  =  LIC2017111XXXXXXXX:66326438736BC7FBCC0C15D9BXXXXXXXXXXXXX          
         失效时间  =  2019-11-22 14:54:24      
     启动紧急详情  =  上限3次，剩余2次            
           序列号  =  LIC2017111XXXXXXXX          
         生成时间  =  2012-01-17 18:20:57          
         产品名称  =  iot9          
         产品版本  =  V200R018CXXXXXXXX          
         网元名称  =  B1XXXXXXXX           
           顺序号  =  1 
(结果个数 = 1)
  
控制项信息 
---------- 
销售项        销售项描述  控制项     控制项描述  当前授权值  授权截止日期   
 
LT1SRANSDC10  销售项BB    basicfun3  NULL        1           2019-12-01     
LT1SRANSDC10  销售项BB    basicfun4  NULL        1           2019-12-01     
LT1SRANSDC10  销售项BB    basicfun4  NULL        1           2019-12-01     
LT1SRANSAA11  销售项CC    basicfun5  NULL        1           2019-12-01     
LT1STU2I2O10  销售项AA    basicres3  NULL        500         2019-12-01     
LT1STU2I2O10  销售项AA    basicres4  NULL        500         2019-12-01     
LT1SRANSAA11  销售项CC    basicres5  NULL        500         2019-12-01     
LT1SRANSAA11  销售项CC    basicres5  NULL        500         2019-12-01     
(结果个数 = 8) 
 
---    END
```

查询当前使用的3.0版本License文件状态信息以及销售项信息：

```
%%DSP LICENSE: DSPBBOM=SALESITEM;%%
RETCODE = 0  操作成功

当前License信息 
---------------          
         当前状态  =  进入宽限期 
已激活License文件  =  license_c20_XXXXXXXXX.xml          
         激活时间  =  2019-11-22 14:22:00        
       设备序列号  =  7CDB4A586DD857F226XXXXXXXXX              
             版本  =  3.0        
       宽限期详情  =  共计60天，剩余57天        
       试用期详情  =  NULL     
    License失效码  =  LIC2017111XXXXXXXX:66326438736BC7FBCC0C15D9BXXXXXXXXXXXXX          
         失效时间  =  2019-11-22 14:54:24      
     启动紧急详情  =  上限3次，剩余2次            
           序列号  =  LIC2017111XXXXXXXX          
         生成时间  =  2012-01-17 18:20:57          
         产品名称  =  iot9          
         产品版本  =  V200R018CXXXXXXXX          
         网元名称  =  B1XXXXXXXX           
           顺序号  =  1 
(结果个数 = 1)
  
销售项信息 
---------- 
销售项        销售项描述  当前控制值  当前使用值  使用率   授权截止日期   
 
LT1SRANSDC10  销售项BB    600         60          10.00%   2021-12-31
LT1SRANSAA11  销售项CC    800         20          25.00%   2021-12-31 
LT1STU2I2O10  销售项AA    500         NULL        NULL     2021-12-31 
(结果个数 = 3) 
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示License(DSP-LICENSE)_00360098.md`
