---
id: UDG@20.15.2@MMLCommand@DSP SFESWMSGSTC
type: MMLCommand
name: DSP SFESWMSGSTC（查询FEISW消息统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFESWMSGSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- FEI消息统计
status: active
---

# DSP SFESWMSGSTC（查询FEISW消息统计）

## 功能

该命令用来查询FEISW消息统计。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：必选参数<br>参数含义：指定系统中有效的资源单元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [FEISW消息统计（SFESWMSGSTC）](configobject/UDG/20.15.2/SFESWMSGSTC.md)

## 使用实例

查询FEISW消息统计：

```
DSP SFESWMSGSTC: RUNAME="VNRS_IPCTRL_EX_RU_0201";
```

```

RETCODE = 0  操作成功。

结果如下
--------
组件ID        子接口                   消息类型    接收消息数量    发送消息数量    IID类型            

0x808c00b4    SSP_SUB_INTF_HA          8           1               0               VOS_IID_MAX        
0x808c00b4    SSP_SUB_INTF_HA          9           1               0               VOS_IID_MAX        
0x808c00b4    SSP_SUB_INTF_HA          11          1               0               VOS_IID_MAX        
0x808c00b4    SSP_SUB_INTF_HA          16          20              0               VOS_IID_MAX        
0x808c00b4    CTL_SUB_INTF_FEISWHAI    1           2               2               VOS_IID_MAX        
0x808c00b4    CTL_SUB_INTF_FEISWHAI    2           2               2               VOS_IID_MAX        
0x808c00b4    CTL_SUB_INTF_FEISWHAI    3           2               2               VOS_IID_MAX        
0x808c00b4    CTL_SUB_INTF_FEISWHAI    5           74              74              VOS_IID_MAX        
0x6a0025      CTL_SUB_INTF_FEII        1           1               1               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FEII        3           29              0               VOS_IID_MAX        
0x6a0025      CTL_SUB_INTF_FEII        5           1               1               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FEII        6           1               2               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FEII        7           1               2               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FEII        4           2               0               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FEII        26          1               1               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FESI        2           6               6               VOS_IID_MAX        
0x6a0025      CTL_SUB_INTF_FESI        6           0               65              VOS_IID_MAX        
0x6a0025      CTL_SUB_INTF_FESI        7           0               2               VOS_IID_MAX        
0x6a0025      CTL_SUB_INTF_FESI        18          1               1               VOS_IID_MAX        
0x6a0025      CTL_SUB_INTF_FESI        19          1               1               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FESI        31          2               1               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FESI        35          1               1               VOS_IID_MAX        
0x8c0026      SMP_SUB_INTF_APPCFGI     3           1               0               VOS_IID_MAX        
0x8c0026      SMP_SUB_INTF_APPCFGI     2           1               0               VOS_IID_MAX        
0x808c00b4    CTL_SUB_INTF_JOBI        1           11              11              VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_LDEVMI      8           61              0               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_LDEVMI      7           40              40              VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_LDEVMI      10          33              0               VOS_IID_MAX        
0x808c00b4    SUB_INTF_MAX             0           4657            0               VOS_IID_TMR_TIMEOUT
(结果个数 = 29)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询FEISW消息统计（DSP-SFESWMSGSTC）_00600789.md`
