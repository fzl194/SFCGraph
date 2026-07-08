---
id: UNC@20.15.2@MMLCommand@LST DDNTHROTTLING
type: MMLCommand
name: LST DDNTHROTTLING（查询DDN Throttling功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DDNTHROTTLING
command_category: 查询类
applicable_nf:
- SGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- DDN Throttling功能开关
status: active
---

# LST DDNTHROTTLING（查询DDN Throttling功能）

## 功能

**适用NF：SGW-C、SMF**

该命令用于查询DDN Throttling功能是否开启。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [DDN Throttling功能（DDNTHROTTLING）](configobject/UNC/20.15.2/DDNTHROTTLING.md)

## 使用实例

假设要查询DDN Throttling功能：

```
%%LST DDNTHROTTLING:;%%
RETCODE = 0  操作成功

DDN Throttling
--------------
DDN Throttling功能开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DDN-Throttling功能（LST-DDNTHROTTLING）_04284711.md`
