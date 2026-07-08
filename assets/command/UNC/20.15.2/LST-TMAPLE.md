---
id: UNC@20.15.2@MMLCommand@LST TMAPLE
type: MMLCommand
name: LST TMAPLE（查询TMAP本地实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TMAPLE
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Tm接口管理
- Tm接口参数管理
status: active
---

# LST TMAPLE（查询TMAP本地实体）

## 功能

**适用网元：MME**

该命令用于查询配置的TMAP本端实体信息。

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMINTFTP | Tm接口类型 | 可选必选说明：必选参数<br>参数含义：集群业务Tm接口类型。<br>数据来源：全网规划<br>取值范围：<br>- “Tm1(用户会话接口)”<br>默认值 ：无<br>配置原则：<br>- Tm1接口需要配置不同的IP地址，作为本端服务IP地址，否则将配置失败。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TMAPLE]] · TMAP本地实体（TMAPLE）

## 使用实例

查询TMAP本地实体Tm1接口记录：

LST TMAPLE:TMINTFTP=Tm1;

```
%%LST TMAPLE:TMINTFTP=Tm1;%% 
RETCODE = 0  操作成功 

操作结果如下
------------------------ 
  Tm接口类型  =  用户会话接口   
  IP地址类型  =  IPV4     
    IPv4地址  =  10.10.10.1  
    IPv6地址  =  ::    
     VPN名称  =  NULL     
    描述信息  =  NULL
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-TMAPLE.md`
