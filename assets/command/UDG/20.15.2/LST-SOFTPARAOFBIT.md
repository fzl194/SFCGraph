---
id: UDG@20.15.2@MMLCommand@LST SOFTPARAOFBIT
type: MMLCommand
name: LST SOFTPARAOFBIT（查询软件参数指定比特位的值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SOFTPARAOFBIT
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务软参管理
- 软件参数比特位
status: active
---

# LST SOFTPARAOFBIT（查询软件参数指定比特位的值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询软件参数某比特位的值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT2 | 软参记录数据类型 | 可选必选说明：必选参数<br>参数含义：软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>默认值：无<br>配置原则：<br>- 配置BYTE表示需要设置字节类型软件参数。<br>- 配置DWORD表示需要设置双字类型软件参数。 |
| PARANUM | 软参号 | 可选必选说明：必选参数<br>参数含义：软参索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1200。当参数类型取值为“BYTE”时，参数索引的取值范围是“1~1200” 当参数类型取值为“DWORD”时，参数索引的取值范围是“1~180”。<br>默认值：无<br>配置原则：无 |
| POSITION | 软参BIT位位置 | 可选必选说明：必选参数<br>参数含义：软参值的指定BIT位位置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。当参数类型取值为“BYTE”，比特位的取值范围是“1~8”。 当参数类型取值为“DWORD”时，比特位的取值范围是“1~32”。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [软件参数指定比特位的值（SOFTPARAOFBIT）](configobject/UDG/20.15.2/SOFTPARAOFBIT.md)

## 使用实例

查询当前参数索引为1的单字节类型软参的第一个比特位的值：

```
LST SOFTPARAOFBIT: DT2=BYTE, PARANUM=1, POSITION=1;
```

```

RETCODE = 0  操作成功

结果如下
--------
  软参记录数据类型  =  BYTE
            软参号  =  1
     软参BIT位位置  =  1
软件参数比特位的值  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询软件参数指定比特位的值（LST-SOFTPARAOFBIT）_86528610.md`
