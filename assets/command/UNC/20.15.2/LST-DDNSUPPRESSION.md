---
id: UNC@20.15.2@MMLCommand@LST DDNSUPPRESSION
type: MMLCommand
name: LST DDNSUPPRESSION（查询DDN抑制功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DDNSUPPRESSION
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- DDN抑制管理
status: active
---

# LST DDNSUPPRESSION（查询DDN抑制功能配置）

## 功能

**适用NF：SGW-C**

该命令用来查询DDN抑制功能配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DDNSUPPRESSION]] · DDN抑制功能配置（DDNSUPPRESSION）

## 使用实例

查询DDN抑制功能配置：

```
%%LST DDNSUPPRESSION:;%%
RETCODE = 0  操作成功

输出结果如下
------------------------
DDN抑制功能开关  =  不使能
   监控时长(分)  =  5
    DDN失败次数  =  10
   抑制时长(分)  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DDNSUPPRESSION.md`
