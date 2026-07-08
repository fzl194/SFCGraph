---
id: UDG@20.15.2@MMLCommand@LST USERSTATISTICS
type: MMLCommand
name: LST USERSTATISTICS（查询用户信息统计功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: USERSTATISTICS
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 业务报表管理
- 用户信息统计管理
- 用户信息统计功能
status: active
---

# LST USERSTATISTICS（查询用户信息统计功能）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示用户信息统计功能的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FUNCTION | 功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- HIGH_RATE_USRSTATS：高带宽用户统计功能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户信息统计功能（USERSTATISTICS）](configobject/UDG/20.15.2/USERSTATISTICS.md)

## 使用实例

查询名为HIGH_RATE_USRSTATS的功能配置信息：

```
%%LST USERSTATISTICS: FUNCTION=HIGH_RATE_USRSTATS;
```

```
%%
RETCODE = 0  操作成功

用户信息统计功能
----------------
         用户瞬间速率的计算周期  =  1000
                       功能开关  =  HIGH_RATE_USRSTATS
               业务信息记录方式  =  DGBCNT
高带宽用户速率门限（兆比特/秒）  =  600
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询用户信息统计功能（LST-USERSTATISTICS）_68773282.md`
