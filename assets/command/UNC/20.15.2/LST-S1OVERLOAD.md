---
id: UNC@20.15.2@MMLCommand@LST S1OVERLOAD
type: MMLCommand
name: LST S1OVERLOAD（查询S1过载控制信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1OVERLOAD
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1接口过载控制
status: active
---

# LST S1OVERLOAD（查询S1过载控制信息）

## 功能

**适用网元：MME**

此命令用于查询配置的MME过载控制策略信息。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@S1OVERLOAD]] · S1接口过载控制（S1OVERLOAD）

## 使用实例

查看S1过载控制信息：

LST S1OVERLOAD:;

```
%%LST S1OVERLOAD:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
一级过载控制策略  =  No control
二级过载控制策略  =  No control
三级过载控制策略  =  No control
四级过载控制策略  =  No control
  等待时长（秒）  =  30
    拒绝比例指示  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-S1OVERLOAD.md`
