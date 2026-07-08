---
id: UDG@20.15.2@MMLCommand@LST FLOWAGETIME
type: MMLCommand
name: LST FLOWAGETIME（查询五元组老化时间）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FLOWAGETIME
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务五元组管理
- 五元组节点老化时间
status: active
---

# LST FLOWAGETIME（查询五元组老化时间）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示头增强五元组、三四层五元组、TCP信令五元组和任意协议五元组的老化时间信息。

## 注意事项

LST FLOWAGETIME查询时间是0则采用任意协议五元组老化时间作为三四层五元组老化时间或者TCP信令五元组老化时间。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/FLOWAGETIME]] · 五元组老化时间（FLOWAGETIME）

## 使用实例

查询五元组老化时间的信息：

```
LST FLOWAGETIME:;
```

```

RETCODE = 0  操作成功。

五元组节点老化时间信息
----------------------
  头增强五元组老化时间（秒）  =  63
  三四层五元组老化时间（秒）  =  8
 TCP信令五元组老化时间（秒）  =  9
任意协议五元组老化时间（秒）  =  60
流量分类五元组老化时间（秒）  =  300
本地分流五元组老化时间（秒）  =  65
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FLOWAGETIME.md`
