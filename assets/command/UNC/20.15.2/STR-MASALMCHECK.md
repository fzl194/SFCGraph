---
id: UNC@20.15.2@MMLCommand@STR MASALMCHECK
type: MMLCommand
name: STR MASALMCHECK（启动5G告警核查）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: MASALMCHECK
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 告警管理
- 告警核查
status: active
---

# STR MASALMCHECK（启动5G告警核查）

## 功能

当发现系统存在未恢复的故障告警时，可通过该命令启动告警核查功能，若系统识别出该故障已经恢复，则自动恢复该故障告警。

当前支持核查的告警包括ALM-100155 HTTP链路故障告警。

## 注意事项

- 该命令执行后立即生效。

- 系统核查速率为每秒20条告警。
- 系统每半个小时会对半小时以前产生的故障告警进行自动核查。
- 命令返回成功表示系统开始核查所有支持核查的故障告警，核查操作将在后台完成。
- 当系统正在核查告警时，该命令返回失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALMTYPE | 告警类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定告警类型。<br>数据来源：本端规划<br>取值范围：<br>- “HTTP_LINKDOWN（HTTP链路故障）”：表示ALM-100155 HTTP链路故障告警，对应的批量告警为ALM-100311 批量HTTP链路故障。<br>- “SUMMARY（汇总）”：表示批量告警的汇总信息。<br>默认值：SUMMARY<br>配置原则：无 |

## 操作的配置对象

- [5G告警核查（MASALMCHECK）](configobject/UNC/20.15.2/MASALMCHECK.md)

## 使用实例

启动告警核查：

```
%%STR MASALMCHECK: ALMTYPE=SUMMARY;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动5G告警核查（STR-MASALMCHECK）_80751076.md`
