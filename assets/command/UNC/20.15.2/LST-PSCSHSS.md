---
id: UNC@20.15.2@MMLCommand@LST PSCSHSS
type: MMLCommand
name: LST PSCSHSS（查询联合接入HSS白名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PSCSHSS
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- 联合接入管理
status: active
---

# LST PSCSHSS（查询联合接入HSS白名单）

## 功能

**适用网元：MME**

该命令用于查询联合接入HSS白名单。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HSSHOST | HSS主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于标识HSS的主机名。<br>数据来源：全网规划<br>取值范围：1~127位字符串。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“.”，其他均为非法字符。<br>默认值：无<br>说明：参数“HSS主机名”大小写不敏感，录入后均转换成大写字母存储和使用。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PSCSHSS]] · 联合接入HSS白名单（PSCSHSS）

## 使用实例

查询联合接入HSS白名单：

```
%%LST PSCSHSS:;%% 
RETCODE = 0  操作成功  
操作结果如下 
------------              
           HSS主机名  =  HUAWEI
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PSCSHSS.md`
