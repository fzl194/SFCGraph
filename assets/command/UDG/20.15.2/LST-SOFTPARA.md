---
id: UDG@20.15.2@MMLCommand@LST SOFTPARA
type: MMLCommand
name: LST SOFTPARA（查询软参记录）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SOFTPARA
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务软参管理
- 软参配置数据管理
status: active
---

# LST SOFTPARA（查询软参记录）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询软件参数信息。

## 注意事项

软参查询不到时，表示软参记录值为0。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT | 软参记录数据类型 | 可选必选说明：可选参数<br>参数含义：软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BIT：比特。<br>- BYTE：字节。<br>- DWORD：双字。<br>- STRING：字符串。<br>默认值：无<br>配置原则：<br>- 配置BIT表示需要查询比特类型软件参数。<br>- 配置BYTE表示需要查询字节类型软件参数。<br>- 配置DWORD表示需要查询双字类型软件参数。<br>- 配置STRING表示需要查询字符串类型软件参数。 |
| DATANUM | 软参记录索引 | 可选必选说明：可选参数<br>参数含义：待查询软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～3840。<br>默认值：无<br>配置原则：<br>- 当DT取值为BIT时，“DATANUM”的取值范围是“1~3840”，当查询范围超过3840则执行失败。<br>- 当DT取值为BYTE时，“DATANUM”的取值范围是“1~1200”，当查询范围在“1200~3840”之间执行成功但是无法查到记录，当查询范围超过3840则执行失败。<br>- 当DT取值为DWORD时，“DATANUM”的取值范围是“1~180”，当查询范围在“180~3840”之间执行成功但是无法查到记录，当查询范围超过3840则执行失败。<br>- 当DT取值为STRING时，“DATANUM”的取值是“1~30”，当查询范围在“30~3840”之间执行成功但是无法查到记录，当查询范围超过3840则执行失败。 |

## 操作的配置对象

- [软参记录（SOFTPARA）](configobject/UDG/20.15.2/SOFTPARA.md)

## 使用实例

查询当前参数索引为1的单字节类型软参的设置情况：

```
LST SOFTPARA: DT=BYTE, DATANUM=1;
```

```

RETCODE = 0  操作成功。

软参记录数据类型  =  字节
    软参记录索引  =  1
      软参记录值  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询软参记录（LST-SOFTPARA）_86528606.md`
