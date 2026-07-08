---
id: UNC@20.15.2@MMLCommand@LST MNO
type: MMLCommand
name: LST MNO（查询MNO配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MNO
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- MNO管理
- MNO配置表
status: active
---

# LST MNO（查询MNO配置信息）

## 功能

**适用网元：SGSN、MME**

该命令用于查询MNO的配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MNOID | MNO标识 | 可选必选说明：可选参数<br>参数含义：待查询MNO的标识。<br>取值范围：0，128~254<br>默认值：无<br>说明：- 0为系统初始值。<br>- 由于系统初始化后，已存在一条“MNOID”为0的记录，当“MNOID”参数为0时，执行[**ADD MNO**](增加MNO配置信息(ADD MNO)_72345671.md)的效果等同于执行[**MOD MNO**](修改MNO配置信息(MOD MNO)_72225751.md)命令<br>- 可以输入参数查询，也可以不输入参数查询。如果输入“MNOID”参数，只是查询这个MNO的配置。如果不输入“MNOID”参数，查询所有的记录。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MNO]] · MNO配置信息（MNO）

## 使用实例

查看所有的MNO:

LST MNO:;

```
%%LST MNO:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
   MNO标识  =  128
运营商全称  =  bbb
运营商简称  =  b
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MNO配置信息(LST-MNO)_26305882.md`
