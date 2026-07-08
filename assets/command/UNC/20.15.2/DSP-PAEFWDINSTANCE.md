---
id: UNC@20.15.2@MMLCommand@DSP PAEFWDINSTANCE
type: MMLCommand
name: DSP PAEFWDINSTANCE（显示PAE转发实例信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEFWDINSTANCE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP PAEFWDINSTANCE（显示PAE转发实例信息）

## 功能

该命令用于显示PAE转发实例信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组; G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENDPOINT | 服务地址 | 可选必选说明：可选参数<br>参数含义：用于指定微服务的实例标识。如果不输入该参数，则显示所有实例信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看服务地址。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PAEFWDINSTANCE]] · PAE转发实例信息（PAEFWDINSTANCE）

## 使用实例

显示PAE转发实例信息：

```
DSP PAEFWDINSTANCE:;
```

```
RETCODE = 0  操作成功。

结果如下
--------
服务地址                              健康检测状态  服务状态  资源ID  部署类型  发布网络标识  健康检查标识  

vup-pod-0                             正常          在线      1112    无状态    是            是            
vup-pod-1                             正常          在线      1113    有状态    是            是            
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PAEFWDINSTANCE.md`
