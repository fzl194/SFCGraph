---
id: UNC@20.15.2@MMLCommand@LST NRFWHITELISTSW
type: MMLCommand
name: LST NRFWHITELISTSW（查询NF白名单开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFWHITELISTSW
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

# LST NRFWHITELISTSW（查询NF白名单开关）

## 功能

**适用NF：NRF**

该命令用于查询NF白名单功能是否开启。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFWHITELISTSW]] · NF白名单开关（NRFWHITELISTSW）

## 使用实例

查询NF白名单功能是否开启。

```
LST NRFWHITELISTSW:;
%%LST NRFWHITELISTSW:;%%
RETCODE = 0  操作成功

结果如下
------------------------
NF白名单开关 =  关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFWHITELISTSW.md`
