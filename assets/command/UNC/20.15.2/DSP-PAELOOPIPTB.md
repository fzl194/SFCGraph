---
id: UNC@20.15.2@MMLCommand@DSP PAELOOPIPTB
type: MMLCommand
name: DSP PAELOOPIPTB（显示Loop口IP和TB映射信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAELOOPIPTB
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

# DSP PAELOOPIPTB（显示Loop口IP和TB映射信息）

## 功能

该命令用于显示Loop口IP TB映射表信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |
| MODULE | 模块名 | 可选必选说明：必选参数<br>参数含义：PAE模块名。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- control：控制面。<br>- forward：转发面。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAELOOPIPTB]] · Loop口IP和TB映射信息（PAELOOPIPTB）

## 使用实例

显示微服务类型为“aa”微服务实例为“aa”的Loop口IP TB映射表信息：

```
DSP PAELOOPIPTB:CELLTYPE="aa", CELLINSTANCE="aa",MODULE=control;
```

```
RETCODE = 0  操作成功。

结果如下
------------------------
IP地址          掩码或前缀长度       目的TB        目的资源ID

192.168.0.1     16                   0x1000000     1     
192.168.0.2     16                   0x40000000    64    
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PAELOOPIPTB.md`
