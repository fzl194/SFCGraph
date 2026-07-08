---
id: UNC@20.15.2@MMLCommand@LST PLMNPRIORITY
type: MMLCommand
name: LST PLMNPRIORITY（查询获取PLMN优先级）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PLMNPRIORITY
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 获取PLMN管理
- 获取PLMN方式的优先级
status: active
---

# LST PLMNPRIORITY（查询获取PLMN优先级）

## 功能

**适用NF：PGW-C、SGW-C、GGSN**

该命令用来查看当前获取GGSN/SGW-C/PGW-C的PLMN标识方式的优先级。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指示UNC的网元形态。<br>数据来源：本端规划<br>取值范围：<br>- GGSN（GGSN）<br>- SGWC（SGW-C）<br>- PGWC（PGW-C）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLMNPRIORITY]] · 获取PLMN优先级（PLMNPRIORITY）

## 使用实例

显示网元类型为GGSN的PLMNPRIORITY的记录：

```
%%LST PLMNPRIORITY: NODETYPE=GGSN;%%
RETCODE = 0  操作成功

结果如下
--------
      网元类型  =  GGSN
  获取PLMN方法  =  LOCAL
GGSN第一优先级  =  SGSN_IP
GGSN第二优先级  =  RAI
GGSN第三优先级  =  ULI
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询获取PLMN优先级（LST-PLMNPRIORITY）_09652282.md`
