---
id: UNC@20.15.2@MMLCommand@DSP PAEPORTBYTB
type: MMLCommand
name: DSP PAEPORTBYTB（显示PAE Fabric端口的TB统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEPORTBYTB
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 端口
status: active
---

# DSP PAEPORTBYTB（显示PAE Fabric端口的TB统计信息）

## 功能

该命令用于显示PAE Fabric端口的TB(Target Board)统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAEPORTBYTB]] · PAE Fabric端口的TB统计信息（PAEPORTBYTB）

## 使用实例

查询微服务类型“aa”微服务实例“bb”的端口统计信息：

```
%%DSP PAEPORTBYTB: CELLTYPE="aa", CELLINSTANCE="bb";%%
RETCODE = 0  操作成功

结果如下:
-------------------------
端口名称        远端TB信息                         接收报文数目                           发送报文数目  
eth2             0x45a                             0                                       0
eth2             0x459                             0                                       0
eth2             0x458                             0                                       0
eth2             0x457                             0                                       0
eth2             0x456                             0                                       0
eth2             0x455                             0                                       0
eth2             0x453                             0                                       0
eth2             0x452                             0                                       0
eth2             0x451                             0                                       0
eth2             0x450                             0                                       0
eth3             0x45a                             0                                       0
eth3             0x459                             0                                       0
eth3             0x458                             0                                       0
eth3             0x457                             0                                       0
eth3             0x456                             0                                       0
eth3             0x455                             524                                   524
eth3             0x453                             0                                       0
eth3             0x452                             0                                       0
eth3             0x451                             0                                       0
eth3             0x450                             0                                       0
(结果个数 = 20)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PAEPORTBYTB.md`
