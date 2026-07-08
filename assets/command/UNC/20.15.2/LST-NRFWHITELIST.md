---
id: UNC@20.15.2@MMLCommand@LST NRFWHITELIST
type: MMLCommand
name: LST NRFWHITELIST（查询NF白名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFWHITELIST
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF白名单配置
status: active
---

# LST NRFWHITELIST（查询NF白名单）

## 功能

**适用NF：NRF**

该命令用于查询NF白名单中的NF实例。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NF白名单（NRFWHITELIST）](configobject/UNC/20.15.2/NRFWHITELIST.md)

## 使用实例

查询白名单中的网元实例列表，执行如下命令：

```
LST NRFWHITELIST:;
%%LST NRFWHITELIST:;%%
RETCODE = 0  操作成功

结果如下
------------------------
NF实例标识  =  instance_01
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF白名单（LST-NRFWHITELIST）_88537098.md`
