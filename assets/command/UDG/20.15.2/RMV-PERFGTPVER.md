---
id: UDG@20.15.2@MMLCommand@RMV PERFGTPVER
type: MMLCommand
name: RMV PERFGTPVER（删除版本粒度的测量对象）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PERFGTPVER
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- Perf GtpVer
status: active
---

# RMV PERFGTPVER（删除版本粒度的测量对象）

## 功能

**适用NF：UPF**

![](删除版本粒度的测量对象（RMV PERFGTPVER）_71791323.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除版本粒度的测量对象可能导致版本粒度的测量指标无法上报。

该命令用于删除版本粒度的测量对象。

## 注意事项

- 该命令执行后立即生效。
- 正常情况下，请勿手动执行该命令。
- 该命令会在升级完成时删除低版本粒度的测量对象。
- 该命令会在回退成功时删除高版本粒度的测量对象。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPVER | 版本 | 可选必选说明：必选参数<br>参数含义：该参数用于表示POD的版本号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PERFGTPVER]] · 版本粒度的测量对象（PERFGTPVER）

## 使用实例

删除版本粒度的测量对象 24.1.0：

```
RMV PERFGTPVER: GTPVER="24.1.0";
RETCODE = 0  操作成功。

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-PERFGTPVER.md`
