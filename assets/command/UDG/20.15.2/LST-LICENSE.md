---
id: UDG@20.15.2@MMLCommand@LST LICENSE
type: MMLCommand
name: LST LICENSE（查询License）
nf: UDG
version: 20.15.2
verb: LST
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

# LST LICENSE（查询License）

## 功能

该命令用于查询数据配置库中License的配置信息。

- 如果不设置“License文件名”参数，则查询系统中License列表信息。
- 如果设置了“License文件名”参数，则查询指定License的详细信息。

> **说明**
> 无

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FN | License文件名称 | 可选必选说明：可选参数。<br>参数含义：用于具体描述一个License文件名称。<br>取值范围：长度为6~311的字符串。文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。<br>默认值：无。<br>配置原则：无。 |
| ST | 源文件类型 | 可选必选说明：可选参数。<br>参数含义：用于指示系统需要按照哪种源类型来查询License文件配置信息。<br>取值范围：<br>- “CURRENTFILE(可用License文件)”：表示查询已上传的，当前系统存在的License文件信息，即在License文件管理页面可见的文件。<br>- “HISTORYFILE(历史激活License文件)”：表示查询License文件激活的历史信息，包含当前激活的License文件。<br>默认值：“CURRENTFILE(可用License文件)”。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LICENSE]] · 失效License（LICENSE）

## 使用实例

查询可用License文件信息：

```
%%LST LICENSE: ST=CURRENTFILE;%%
RETCODE = 0  操作成功

License文件列表
---------------
License文件名称    是否为当前License文件   激活时间              文件类型     License序列号        文件生成时间              产品名称     产品版本

License_xx1.xml    是                      2019-11-01 08:00:30   商用         LIC201911010001X2    2019-10-10  20:20:20      IVS          V100R019
License_xx2.xml    否                      NULL                  调测         LIC201911010002X2    2019-10-10  20:20:20      IVS          V100R019
License_xx3.xml    否                      NULL                  商用         LIC201911010002X2    2019-10-10  20:20:20      IVS          V100R019
(结果个数 = 3)
 
---    END
```

查询历史激活License文件信息：

```
%%LST LICENSE: ST=HISTORYFILE;%%
RETCODE = 0  操作成功
 
License文件列表
---------------
License文件名称    是否为当前License文件   激活时间              文件类型     License序列号        文件生成时间              产品名称     产品版本

License_xx1.xml    是                      2019-11-03 08:00:30   商用         LIC201911010001X2    2019-10-10  20:20:20      IVS          V100R019
License_xx2.xml    否                      2019-11-02 08:00:30   调测         LIC201911010002X2    2019-10-10  20:20:20      IVS          V100R019
License_xx3.xml    否                      2019-11-01 08:00:30   商用         LIC201911010003X2    2019-10-10  20:20:20      IVS          V100R019
(结果个数 = 3)
 
---    END
```

查询指定3.0版本可用License文件“License_xx1.xml”信息：

```
%%LST LICENSE: FN="License_xx1.xml", ST=CURRENTFILE;%%
RETCODE = 0  操作成功
 
License文件信息
---------------
License文件名称  =  License_xx1.xml
           国家  =  English
         运营商  =  RD of Huawei Technologies Co., Ltd
           局点  =  ShenZhen
         创建者  =  Huawei Technologies Co., Ltd
  License序列号  =  LIC201910XXXXXXXXX
     设备序列号  =  21BF60C4B8AF90EF850C2700EXXXXXXXXXXX
   文件生成时间  =  2019-10-23 09:59:21
       产品名称  =  XXXXX
(结果个数 = 1)
 
控制项信息
----------
销售项                授权截止日期      控制项            控制项描述                  控制值

HSSRF1                2019-11-11        basicfun3         基本软件1                   200
HSSRF2                2019-11-11        basicfun4         基本软件2                   200
HSSRF3                2019-11-11        basicfun5         基本软件3                   200
(结果个数 = 3)
 
---    END
```

查询指定3.0版本历史激活License文件“License_xx1.xml”信息：

```
%%LST LICENSE: FN="License_xx1.xml", ST=HISTORYFILE;%%
RETCODE = 0  操作成功
 
License文件信息
---------------
License文件名称  =  License_xx1.xml
           国家  =  English
         运营商  =  RD of Huawei Technologies Co., Ltd
           局点  =  ShenZhen
         创建者  =  Huawei Technologies Co., Ltd
  License序列号  =  LIC201910XXXXXXXXX
     设备序列号  =  21BF60C4B8AF90EF850C2700EXXXXXXXXXXX
   文件生成时间  =  2019-10-23 09:59:21
       产品名称  =  XXXXX
(结果个数 = 1)
 
控制项信息
----------
销售项                授权截止日期      控制项            控制项描述                  控制值

HSSRF1                2019-11-11        basicfun3         基本软件1                   200
HSSRF2                2019-11-11        basicfun4         基本软件2                   200
HSSRF3                2019-11-11        basicfun5         基本软件3                   200
(结果个数 = 3)
 
---    END
```

查询指定2.0版本当前可用License文件“License_xx1.dat”信息：

```
%%LST LICENSE: FN="License_xx1.dat", ST=CURRENTFILE;%%
RETCODE = 0  操作成功
 
License文件信息
---------------
License文件名称  =  License_xx1.dat
           国家  =  English
         运营商  =  RD of Huawei Technologies Co., Ltd
           局点  =  ShenZhen
         创建者  =  Huawei Technologies Co., Ltd
  License序列号  =  LIC20191023XXXXXXX
     设备序列号  =  21BF60C4B8AF90EF850C2700E17FXXXXXX
   文件生成时间  =  2019-10-23 09:59:21
       产品名称  =  IXXXXXX
           注释  =  Order XXXXXXXXXX
(结果个数 = 1)
 
控制项信息
----------
特征项                  授权截止日期           属性                    控制项         控制项描述                  控制值

HSSRF1                  2019-11-11             DEMO, 2019-11-23, 60    basicfun3      基本软件1                    200
HSSRF2                  2019-11-11             DEMO, 2019-11-23, 60    basicfun4      基本软件2                    200
HSSRF3                  2019-11-11             DEMO, 2019-11-23, 60    basicfun5      基本软件3                    200 
(结果个数 = 3)

---    END
```

查询指定2.0版本历史激活License文件“License_xx1.dat”信息：

```
%%LST LICENSE: FN="License_xx1.dat", ST=HISTORYFILE;%%
RETCODE = 0  操作成功
 
License文件信息
---------------
License文件名称  =  License_xx1.dat
           国家  =  English
         运营商  =  RD of Huawei Technologies Co., Ltd
           局点  =  ShenZhen
         创建者  =  Huawei Technologies Co., Ltd
  License序列号  =  LIC20191023XXXXXXX
     设备序列号  =  21BF60C4B8AF90EF850C2700E17FXXXXXX
   文件生成时间  =  2019-10-23 09:59:21
       产品名称  =  IXXXXXX
           注释  =  Order XXXXXXXXXX
(结果个数 = 1)
 
控制项信息
----------
特征项                  授权截止日期           属性                    控制项         控制项描述                  控制值

HSSRF1                  2019-11-11             DEMO, 2019-11-23, 60    basicfun3      基本软件1                    200
HSSRF2                  2019-11-11             DEMO, 2019-11-23, 60    basicfun4      基本软件2                    200
HSSRF3                  2019-11-11             DEMO, 2019-11-23, 60    basicfun5      基本软件3                    200 
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询License(LST-LICENSE)_00220006.md`
