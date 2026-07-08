---
id: UNC@20.15.2@MMLCommand@LST ROAMCOMMPLCY
type: MMLCommand
name: LST ROAMCOMMPLCY（查询漫游通信策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ROAMCOMMPLCY
command_category: 查询类
applicable_nf:
- AMF
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 漫游通信模式管理
- 漫游通信策略管理
status: active
---

# LST ROAMCOMMPLCY（查询漫游通信策略）

## 功能

**适用NF：AMF、SMF**

该命令用于显示漫游通信策略信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROAMCOMMPLCY]] · 漫游通信策略（ROAMCOMMPLCY）

## 使用实例

运营商需要查询漫游通信策略；

```
%%LST ROAMCOMMPLCY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
漫游路由模式 = 通过SEPP通信
信令汇聚模式 = Http Proxy
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ROAMCOMMPLCY.md`
