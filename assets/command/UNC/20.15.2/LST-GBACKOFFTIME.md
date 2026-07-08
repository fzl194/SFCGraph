---
id: UNC@20.15.2@MMLCommand@LST GBACKOFFTIME
type: MMLCommand
name: LST GBACKOFFTIME（查询全局Back-off Time信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GBACKOFFTIME
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
- 接入管理运维
- 流控管理
- 全局Back-off Time信息
status: active
---

# LST GBACKOFFTIME（查询全局Back-off Time信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查看全局Back-off Time信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [全局Back-off Time信息（GBACKOFFTIME）](configobject/UNC/20.15.2/GBACKOFFTIME.md)

## 使用实例

查询全局Back-off Time信息：

```
%%LST GBACKOFFTIME:;%%
RETCODE = 0  操作成功

结果如下
--------
全局Back-off 时长(秒)  =  600
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局Back-off-Time信息（LST-GBACKOFFTIME）_76686930.md`
