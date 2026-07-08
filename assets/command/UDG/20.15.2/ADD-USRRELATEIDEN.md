---
id: UDG@20.15.2@MMLCommand@ADD USRRELATEIDEN
type: MMLCommand
name: ADD USRRELATEIDEN（增加用户关联识别）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: USRRELATEIDEN
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 用户关联识别
status: active
---

# ADD USRRELATEIDEN（增加用户关联识别）

## 功能

**适用NF：PGW-U、UPF**

该命令用于新增指定的protocol的用户关联配置，对某些识别率诉求特别高的加密类应用，需要开启用户关联识别功能提升识别准确率时配置该命令。

## 注意事项

- 该命令执行后60s生效。
- 总记录数最大为64。
- 只能对支持该功能的协议进行配置，如果指定的用户关联识别协议，不支持其开启关联功能，但不会执行失败。可以用LST SUPPUSRRLTIDEN命令查询支持用户关联识别的协议列表。
- 用户关联识别功能如果指定的协议过多，会影响系统性能，具体下降比例与话务模型相关。如果没有内容计费等特别高的计费诉求，不建议开启。
- 按需开启软参BIT387以开启双栈用户二元组关联识别功能。
- 该命令只支持2，3级协议。
- 该命令依赖知识库文件加载成功。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLNAME | 协议名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置对应的协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：当需要新增用户关联识别配置时配置该参数。 |
| USRRLTIDENSW | 用户关联识别开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否开启用户关联识别功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：关闭用户关联识别功能。<br>- ENABLE：开启用户关联识别功能。<br>默认值：无<br>配置原则：<br>- DISABLE：关闭对应协议的用户关联识别功能，用户关联识别功能如果指定的协议过多，会影响性能，具体下降比例与话务模型相关。如果没有内容计费等特别高的计费诉求，建议关闭。<br>- ENABLE：开启用户关联识别功能，如果运营商需要通过开启用户关联识别功能，来增强对部分加密业务流的协议识别能力时开启。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@USRRELATEIDEN]] · 用户关联识别（USRRELATEIDEN）

## 关联任务

- [[UDG@20.15.2@Task@0-00153]]

## 使用实例

假设运营商的某个应用需要对https协议提升识别准确率时，需要新增指定protocol的用户关联识别功能：

```
ADD USRRELATEIDEN: PROTOCOLNAME="https",USRRLTIDENSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-USRRELATEIDEN.md`
