---
id: UNC@20.15.2@MMLCommand@SET NSSFRTNSMAXNUM
type: MMLCommand
name: SET NSSFRTNSMAXNUM（设置NSSF响应切片最大数量配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NSSFRTNSMAXNUM
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF功能参数配置
status: active
---

# SET NSSFRTNSMAXNUM（设置NSSF响应切片最大数量配置）

## 功能

**适用NF：NSSF**

该命令用于配置NSSF响应切片最大长度信息。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ALLOWEDNSMAXNUM |
| --- |
| 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALLOWEDNSMAXNUM | Allowed切片最大数量 | 可选必选说明：可选参数<br>参数含义：该参数用于控制切片选择流程响应中Allowed切片最大数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSSFRTNSMAXNUM查询当前参数配置值。<br>配置原则：<br>该参数配置为0，表示不限制切片选择流程中响应Allowed切片个数。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFRTNSMAXNUM]] · NSSF响应切片最大数量配置（NSSFRTNSMAXNUM）

## 使用实例

假如运营商希望修改Allowed切片最大数量为8，执行以下命令。

```
SET NSSFRTNSMAXNUM: ALLOWEDNSMAXNUM=8;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置NSSF响应切片最大数量配置（SET-NSSFRTNSMAXNUM）_97901496.md`
