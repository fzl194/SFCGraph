---
id: UNC@20.15.2@MMLCommand@LST COMMTRCCTRL
type: MMLCommand
name: LST COMMTRCCTRL（查询通用模块跟踪控制功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: COMMTRCCTRL
command_category: 查询类
applicable_nf:
- AMF
- SMF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- OM调测
status: active
---

# LST COMMTRCCTRL（查询通用模块跟踪控制功能）

## 功能

**适用NF：AMF、SMF、SMSF、NCG**

该命令用于查询通用模块跟踪功能控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/COMMTRCCTRL]] · 通用模块跟踪控制功能（COMMTRCCTRL）

## 使用实例

查询通用模块跟踪控制功能，执行如下命令：

```
%%LST COMMTRCCTRL:;%%
RETCODE = 0  操作成功

结果如下
------------------------
     E2E跟踪不上报开关  =  NULL
    接口跟踪不上报开关  =  NULL
    用户跟踪不上报开关  =  NULL
    随机跟踪不上报开关  =  NULL
上报跟踪流控的消息开关  =  OFF
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-COMMTRCCTRL.md`
