---
id: UNC@20.15.2@MMLCommand@LST EXTENDQCIMAP
type: MMLCommand
name: LST EXTENDQCIMAP（查询扩展QCI和标准QCI的映射关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EXTENDQCIMAP
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 扩展QCI功能
- 扩展QCI和标准QCI映射
status: active
---

# LST EXTENDQCIMAP（查询扩展QCI和标准QCI的映射关系）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询扩展QCI和标准QCI的映射关系，并查询扩展QCI的优先级。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXTENDQCI | 扩展QCI的值 | 可选必选说明：可选参数<br>参数含义：该参数用来指定扩展QCI。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是10~255。<br>默认值：无<br>配置原则：<br>该参数值不能与命令ADD STDQOSID中配置的QoS ID一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EXTENDQCIMAP]] · 扩展QCI和标准QCI的映射关系（EXTENDQCIMAP）

## 使用实例

查询“扩展QCI”与“标准QCI”的对应关系。指定“扩展QCI”为“133”：

```
%%LST EXTENDQCIMAP: EXTENDQCI=133;%%
RETCODE = 0  操作成功

结果如下
--------
    扩展QCI的值  =  133
    标准QCI的值  =  1
扩展QCI的优先级  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-EXTENDQCIMAP.md`
