---
id: UDG@20.15.2@MMLCommand@LST ARPANTISPOOFING
type: MMLCommand
name: LST ARPANTISPOOFING（查询ARP防欺骗信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ARPANTISPOOFING
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP防欺骗配置
status: active
---

# LST ARPANTISPOOFING（查询ARP防欺骗信息）

## 功能

该命令用于查询ARP防欺骗功能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/ARPANTISPOOFING]] · ARP防欺骗信息（ARPANTISPOOFING）

## 使用实例

查询ARP防欺骗配置信息：

```
LST ARPANTISPOOFING:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
    ARP防欺骗使能  =  去使能
      ARP探测次数  =  5
ARP防欺骗告警使能  =  去使能
      ARP冲突阈值  =  30
    老化时间（s）  =  1200
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ARPANTISPOOFING.md`
