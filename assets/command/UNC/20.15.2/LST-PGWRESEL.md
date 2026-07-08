---
id: UNC@20.15.2@MMLCommand@LST PGWRESEL
type: MMLCommand
name: LST PGWRESEL（查询本地P-GW重选策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PGWRESEL
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 本地P-GW重选功能配置
status: active
---

# LST PGWRESEL（查询本地P-GW重选策略）

## 功能

**适用网元：MME**

该命令用于查询本地P-GW重选策略的配置记录。

## 注意事项

无

## 权限

manage-ug；system-ug ；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN网络标识，不输入表示查询所有记录。<br>数据来源：全网规划<br>取值范围：1~62位字符串<br>默认值：无<br>说明：- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PGWRESEL]] · 本地P-GW重选策略（PGWRESEL）

## 使用实例

查询所有本地P-GW重选策略配置记录：

LST PGWRESEL:;

```
%%LST PGWRESEL:;%%
RETCODE = 0  操作成功。

查询结果如下
-------------------------
                APN网络标识  =  HUAWEI
          区域标识起始Label  =  1
          区域标识终止Label  =  2
                   触发条件  =  根据指定时间
                   起始时间  =  18:00:00
                   结束时间  =  19:00:00
   ECM-IDLE状态时间阈值(秒)  =  60
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PGWRESEL.md`
