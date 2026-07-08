---
id: UNC@20.15.2@MMLCommand@CLR NRFNFATTRVRY
type: MMLCommand
name: CLR NRFNFATTRVRY（清除NF属性冲突核验记录）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: NRFNFATTRVRY
command_category: 动作类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF属性冲突核验
status: active
---

# CLR NRFNFATTRVRY（清除NF属性冲突核验记录）

## 功能

**适用NF：NRF**

该命令用于清除NF属性冲突核验结果历史记录和取消当前正在进行的冲突核验。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示进行属性冲突核验的NF实例标识，如果输入具体NF实例标识，。<br>代表只清除该NF的核验历史记录，若当前NF正在核验，则取消核验并清除记录。<br>如果不输入表示清除所有的NF核验历史数据，正在核验的NF取消核验并清除记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~36。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFNFATTRVRY]] · 操作执行NF属性冲突核验（NRFNFATTRVRY）

## 使用实例

清除并取消NF属性冲突核验：

```
CLR NRFNFATTRVRY: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-NRFNFATTRVRY.md`
