---
id: UDG@20.15.2@MMLCommand@LST UDGNRMINTF
type: MMLCommand
name: LST UDGNRMINTF（查询逻辑口）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UDGNRMINTF
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 逻辑接口管理
- 逻辑接口配置
- 备份逻辑接口
status: active
---

# LST UDGNRMINTF（查询逻辑口）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询逻辑口记录。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTNAME | 保留逻辑接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置保留的逻辑接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UDGNRMINTF]] · 逻辑口（UDGNRMINTF）

## 使用实例

假设需要查询名称为pgwusxif的逻辑口记录，配置如下：

```
LST UDGNRMINTF: INTNAME="pgwusxif";
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
          保留逻辑接口名称  =  pgwusxif
                 网元类型  =  PGWU
                 接口类型  =  Sx
       逻辑接口的IPv4地址1  =  127.127.127.127
       逻辑接口的IPv4地址2  =  0.0.0.0
       逻辑接口的IPv4地址3  =  0.0.0.0
       逻辑接口的IPv4地址4  =  0.0.0.0
       逻辑接口的IPv4地址5  =  0.0.0.0
       逻辑接口的IPv6地址1  =  ::
       逻辑接口的IPv6地址2  =  ::
       逻辑接口的IPv6地址3  =  ::
       逻辑接口的IPv6地址4  =  ::
       逻辑接口的IPv6地址5  =  ::
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UDGNRMINTF.md`
