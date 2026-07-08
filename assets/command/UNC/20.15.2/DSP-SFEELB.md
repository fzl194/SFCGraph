---
id: UNC@20.15.2@MMLCommand@DSP SFEELB
type: MMLCommand
name: DSP SFEELB（显示ELB表项）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SFEELB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE表项统计
status: active
---

# DSP SFEELB（显示ELB表项）

## 功能

该命令用于显示ELB表项。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MGID | 组播组ID | 可选必选说明：必选参数<br>参数含义：该参数表示组播叶子ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SEQNUM | 序号 | 可选必选说明：必选参数<br>参数含义：该参数表示叶子序号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| WORKMODE | 工作模式 | 可选必选说明：必选参数<br>参数含义：该参数表示工作模式；0为主，1为备。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [ELB表项（SFEELB）](configobject/UNC/20.15.2/SFEELB.md)

## 使用实例

显示指定资源单元、指定组播组ID、序列号、主备模式的ELB表项：

```
DSP SFEELB:MGID=100,SEQNUM=1024,WORKMODE=1,RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。
                                                                                
结果如下
------------------------
组播组ID  =  100
    序号  =  1024
工作模式  =  1 
    结果  =    
              *TmgId : 00000064                             *SN : 00000400            
           *WorkType : 01                                 Valid : 01                  
            ElbIndex : 00000001                              PT : 00                  
                  TB : 0041                                  TP : 0008           

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示ELB表项（DSP-SFEELB）_50280730.md`
