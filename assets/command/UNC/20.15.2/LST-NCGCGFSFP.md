---
id: UNC@20.15.2@MMLCommand@LST NCGCGFSFP
type: MMLCommand
name: LST NCGCGFSFP（查询软参）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NCGCGFSFP
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- NCG大颗粒软参
status: active
---

# LST NCGCGFSFP（查询软参）

## 功能

**适用NF：NCG**

该命令用于查询当前配置的NCG大颗粒软参信息。

- 若需要查询全部软件参数信息，请不要输入任何参数。
- 若需要查询某一软件参数的详细信息，请输入“软参ID”。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SFPID | 软参ID | 可选必选说明：可选参数<br>参数含义：用于表示NCG大颗粒软参ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4999。<br>默认值：无<br>配置原则：无 |
| SFPVALUE | 软参值 | 可选必选说明：可选参数<br>参数含义：用于表示NCG大颗粒软参值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCGCGFSFP]] · 软参（NCGCGFSFP）

## 使用实例

查询“软参ID”为“1”的软参值：

```
LST NCGCGFSFP: SFPID=1;
```

```
RETCODE = 0  操作成功

结果如下:
```

```
软参ID  =  1
软参值  =  10
--------

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NCGCGFSFP.md`
