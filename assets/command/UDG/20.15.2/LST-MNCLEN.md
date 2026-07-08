---
id: UDG@20.15.2@MMLCommand@LST MNCLEN
type: MMLCommand
name: LST MNCLEN（显示MNC长度信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MNCLEN
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- UP信息管理
- MNC长度
status: active
---

# LST MNCLEN（显示MNC长度信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查看MCC号对应的MNC长度。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，为3位数字，000～999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MNCLEN]] · MNC长度信息（MNCLEN）

## 使用实例

查看当前UPF所属的MCC的MNC长度：

```
LST MNCLEN:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
      移动国家码  =  460
对应MCC的MNC长度  =  2
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示MNC长度信息（LST-MNCLEN）_44865464.md`
