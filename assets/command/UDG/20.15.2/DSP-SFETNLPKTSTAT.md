---
id: UDG@20.15.2@MMLCommand@DSP SFETNLPKTSTAT
type: MMLCommand
name: DSP SFETNLPKTSTAT（显示SFE隧道报文统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFETNLPKTSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 统计信息
status: active
---

# DSP SFETNLPKTSTAT（显示SFE隧道报文统计）

## 功能

该命令用来显示转发隧道报文统计。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| TUNNELINDEX | 隧道索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定隧道索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [SFE隧道报文统计（SFETNLPKTSTAT）](configobject/UDG/20.15.2/SFETNLPKTSTAT.md)

## 使用实例

显示转发隧道报文统计：

```
DSP SFETNLPKTSTAT: RUNAME="VNODE_VNRS_VNFC_IPU_0064", TUNNELINDEX=64;
```

```

RETCODE = 0  操作成功.                                                                                                     
结果如下 

------------------------
          RU名称  =  VNODE_VNRS_VNFC_IPU_0064
      入报文个数  =  0
    入报文字节数  =  0
    入单播报文数  =  0
    入多播报文数  =  0
    入广播报文数  =  0
入单播丢弃报文数  =  0
入多播丢弃报文数  =  0
入广播丢弃报文数  =  0
      出报文个数  =  0
    出报文字节数  =  0
    出单播报文数  =  0
    出多播报文数  =  0
    出广播报文数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示SFE隧道报文统计（DSP-SFETNLPKTSTAT）_49802594.md`
