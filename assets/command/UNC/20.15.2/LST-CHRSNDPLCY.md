---
id: UNC@20.15.2@MMLCommand@LST CHRSNDPLCY
type: MMLCommand
name: LST CHRSNDPLCY（查询CHR传输策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHRSNDPLCY
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- CHR管理
- CHR传输策略
status: active
---

# LST CHRSNDPLCY（查询CHR传输策略）

## 功能

**适用网元：SGSN、MME**

该命令用于查询CHR传输策略。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入任何参数，执行该命令会显示所有记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | CHR传输策略类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CHR传输策略类型。<br>数据来源：本端规划<br>取值范围：<br>- “APNNI（签约APNNI）”：表示签约数据指定的APNNI的用户的CHR单据才会传输给CloudUDN。<br>默认值：无<br>配置原则：当前仅支持配置“签约APNNI” |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHRSNDPLCY]] · CHR传输策略（CHRSNDPLCY）

## 使用实例

查询CHR传输策略：

LST CHRSNDPLCY:;

```
%%LST CHRSNDPLCY:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
CHR传输策略类型  =  签约APNNI
    APN网络标识  =  HUAWEI.COM
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CHR传输策略(LST-CHRSNDPLCY)_72225293.md`
