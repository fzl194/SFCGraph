---
id: UNC@20.15.2@MMLCommand@LST CPGTPUPARA
type: MMLCommand
name: LST CPGTPUPARA（查询GTPU参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CPGTPUPARA
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N4 GTP-U管理
- N4 GTP-U路径参数管理
status: active
---

# LST CPGTPUPARA（查询GTPU参数）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询GTPU参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/CPGTPUPARA]] · GTPU参数（CPGTPUPARA）

## 使用实例

查询GTPU参数

```
LST CPGTPUPARA:;

%%LST CPGTPUPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
		主动发送路径探测消息开关  =  开
			路径探测消息间隔(秒)  =  60
	路径探测消息重发时间间隔(秒)  =  3
		路径探测消息最大重试次数  =  3
	  路径故障后去激活上下文开关  =  开
			  故障后重试探测次数  =  30
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTPU参数（LST-CPGTPUPARA）_13800466.md`
