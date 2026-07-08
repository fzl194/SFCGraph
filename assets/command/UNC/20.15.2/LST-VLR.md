---
id: UNC@20.15.2@MMLCommand@LST VLR
type: MMLCommand
name: LST VLR（查询VLR配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLR
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- VLR管理
status: active
---

# LST VLR（查询VLR配置信息）

## 功能

**适用网元：SGSN、MME**

该命令用于查询与本局 UNC 相连的VLR的信息。

## 注意事项

若查询全部记录，无需输入参数；若需查询单条记录输入参数VLR号。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VN | VLR号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VLR在移动网络中的设备号。<br>数据来源：整网规划<br>取值范围： 1～15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLR]] · VLR配置信息（VLR）

## 使用实例

查询所有与SGSN相连的VLR信息：

**LST VLR:;**

```
%%LST VLR:;%%
RETCODE = 0  操作成功。

VLR表
-----
 VLR号           VLR名称  Sv/SGs合一  MSC主机名  MSC POOL名称  最小V值  最大V值  SGs主叫通知功能  CSFB被叫恢复功能

 86139006201      vlr1    不合一       NULL       pool1         0        200      不支持          支持
 86139006202      vlr2    不合一       NULL       pool1         201      999      支持            支持
 (结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VLR配置信息(LST-VLR)_72225125.md`
