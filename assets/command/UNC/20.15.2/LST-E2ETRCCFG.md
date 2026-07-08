---
id: UNC@20.15.2@MMLCommand@LST E2ETRCCFG
type: MMLCommand
name: LST E2ETRCCFG（查询端到端用户跟踪参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: E2ETRCCFG
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 跟踪配置管理
- 端到端用户跟踪管理
status: active
---

# LST E2ETRCCFG（查询端到端用户跟踪参数）

## 功能

**适用网元：MME**

本命令用于查询端到端用户跟踪参数。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@E2ETRCCFG]] · 端到端用户跟踪参数（E2ETRCCFG）

## 使用实例

查询端到端用户跟踪参数：

LST E2ETRCCFG:;

```
%%LST E2ETRCCFG:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
 是否上报SGs接口消息  =  是
  是否上报Sv接口消息  =  是
基站上报寻呼消息开关  =  关
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-E2ETRCCFG.md`
