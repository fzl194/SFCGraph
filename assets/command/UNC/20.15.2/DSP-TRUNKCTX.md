---
id: UNC@20.15.2@MMLCommand@DSP TRUNKCTX
type: MMLCommand
name: DSP TRUNKCTX（显示宽带集群系统上下文）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TRUNKCTX
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 用户数据库管理
status: active
---

# DSP TRUNKCTX（显示宽带集群系统上下文）

## 功能

**适用NF：MME**

该命令用于查看MME和TSN之间的建立信息以及UE当前在TSN上的状态。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数ID | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数说明：该参数用于指定国际移动用户标识。<br>取值范围：1～15位数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TRUNKCTX]] · 宽带集群系统上下文（TRUNKCTX）

## 使用实例

1. 获取宽带集群系统上下文：
  ```
  DSP TRUNKCTX: IMSI="123031601000001";
  ```
  ```
  查询结果如下
  ------------------------
   UE与TSN之间是否建立了连接  =  否
    UE与TSN之间连接的TSN标识  =  NULL
   UE与TSN之间连接的建立时间  =  2000-01-01 08:00:00+08:00
            集群终端协议版本  =  版本1
            UE当前的遥开状态  =  遥开
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-TRUNKCTX.md`
