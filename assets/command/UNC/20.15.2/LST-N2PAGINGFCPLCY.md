---
id: UNC@20.15.2@MMLCommand@LST N2PAGINGFCPLCY
type: MMLCommand
name: LST N2PAGINGFCPLCY（查询N2模式寻呼消息反压流控策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N2PAGINGFCPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- N2模式反压流控管理
status: active
---

# LST N2PAGINGFCPLCY（查询N2模式寻呼消息反压流控策略）

## 功能

**适用NF：AMF**

该命令用于查询N2模式寻呼反压流控功能的相关策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@N2PAGINGFCPLCY]] · N2模式寻呼消息反压流控策略（N2PAGINGFCPLCY）

## 使用实例

查询当前系统的N2模式寻呼消息反压流控策略，执行如下命令：

```
%%LST N2PAGINGFCPLCY:;%%
RETCODE = 0  操作成功

结果如下
----------------------
N2寻呼反压流控功能开关 = 开启
      精准寻呼控制开关 = 开启
      寻呼重发控制开关 = 开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-N2PAGINGFCPLCY.md`
