---
id: UNC@20.15.2@MMLCommand@LST NRFNFLSTCTLPLY
type: MMLCommand
name: LST NRFNFLSTCTLPLY（查询NFINFOLIST处理策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFNFLSTCTLPLY
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF多INFO管理策略
status: active
---

# LST NRFNFLSTCTLPLY（查询NFINFOLIST处理策略）

## 功能

**适用NF：NRF**

该命令用于查询NF携带NFINFOLIST注册、更新、发现策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示携带NFINFOLIST注册、更新、发现策略对应的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- SMF（SMF）<br>- NWDAF（NWDAF）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNFLSTCTLPLY]] · NFINFOLIST处理策略（NRFNFLSTCTLPLY）

## 使用实例

运营商需查询NF携带NFINFOLIST后注册、更新、发现策略时，执行如下命令：

```
LST NRFNFLSTCTLPLY:;
            %%LST NRFNFLSTCTLPLY:;%%
            RETCODE = 0  操作成功

            结果如下
            --------
            网元类型  携带NFINFOLIST注册更新处理策略      服务发现优先匹配NFINFO开关  注册更新多NFINFO部分无TAI处理开关

            SMF       不检验NFINFO或NFINFOLIST的携带情况  打开                        打开
            NWDAF     不检验NFINFO或NFINFOLIST的携带情况  关闭                        打开
            (结果个数 = 2)

            ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NFINFOLIST处理策略（LST-NRFNFLSTCTLPLY）_23622950.md`
