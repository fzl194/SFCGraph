---
id: UNC@20.15.2@MMLCommand@DSP SECTOTALPKTTAB
type: MMLCommand
name: DSP SECTOTALPKTTAB（显示安全总报文表项）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SECTOTALPKTTAB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略总报文
status: active
---

# DSP SECTOTALPKTTAB（显示安全总报文表项）

## 功能

该命令用来显示总报文表项。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECTOTALPKTTAB]] · 安全总报文表项（SECTOTALPKTTAB）

## 使用实例

显示安全总报文表项：

```
DSP SECTOTALPKTTAB:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```
RETCODE = 0  操作成功.  
                                                                                                   
结果如下 
------------------------
        RU名称  =  VNODE_VNRS_VNFC_IPU_0064
    当前策略ID  =  1
CAR速率（pps）  =  6000
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SECTOTALPKTTAB.md`
