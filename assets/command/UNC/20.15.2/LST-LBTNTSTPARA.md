---
id: UNC@20.15.2@MMLCommand@LST LBTNTSTPARA
type: MMLCommand
name: LST LBTNTSTPARA（查询CSLB隧道探测参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LBTNTSTPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 隧道管理
- CSLB隧道探测参数
status: active
---

# LST LBTNTSTPARA（查询CSLB隧道探测参数）

## 功能

该命令用于查询CSLB隧道探测参数。

## 注意事项

- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [CSLB隧道探测参数（LBTNTSTPARA）](configobject/UNC/20.15.2/LBTNTSTPARA.md)

## 使用实例

查询CSLB隧道探测参数。

LST LBTNTSTPARA:;

```
%%LST LBTNTSTPARA:;%%
RETCODE = 0  操作成功。

操作结果如下：
--------------
  隧道时延探测周期（秒）  =  10
隧道丢包率统计周期（秒）  =  5
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CSLB隧道探测参数（LST-LBTNTSTPARA）_50911923.md`
