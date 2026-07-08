---
id: UNC@20.15.2@MMLCommand@LST NFDISCSCHEMEPLY
type: MMLCommand
name: LST NFDISCSCHEMEPLY（查询服务发现Scheme优选策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFDISCSCHEMEPLY
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- NF发现Scheme优选策略管理
status: active
---

# LST NFDISCSCHEMEPLY（查询服务发现Scheme优选策略）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询服务发现时的Scheme优选策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INFOTYPE | 信息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定信息类型。<br>数据来源：本端规划<br>取值范围：<br>- “BYNFTYPE（使用NF类型）”：输入NF类型<br>- “BYNFID（使用NF实例标识）”：输入NF实例标识<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFDISCSCHEMEPLY]] · 服务发现Scheme优选策略（NFDISCSCHEMEPLY）

## 使用实例

- 查询所有服务发现时的Scheme优选策略。
  ```
  %%LST NFDISCSCHEMEPLY:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  信息类型  		NF类型     NF实例标识      服务名称                                    策略      

  使用NF类型		NfUDM      NULL            UDM提供的Nudm_SubscriberDataManagement服务  仅HTTP   
  使用NF实例标识	NfInvalid  smf_instance_0  SMF提供的Nsmf_PDUSession服务                仅HTTPS  
  (结果个数 = 2)

  ---    END
  ```
- 查询所有根据NF类型配置的服务发现时的Scheme优选策略。
  ```
  %%LST NFDISCSCHEMEPLY: INFOTYPE=BYNFTYPE;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
       NF类型  =  NfUDM
  服务名称  =  UDM提供的Nudm_SubscriberDataManagement服务
       策略  =  仅HTTP
  (结果个数 = 1)

  ---    END
  ```
- 查询所有根据NF实例标识配置的服务发现时的Scheme优选策略。
  ```
  %%LST NFDISCSCHEMEPLY: INFOTYPE=BYNFID;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  NF实例标识  =  smf_instance_0
   服务名称  =  SMF提供的Nsmf_PDUSession服务
        策略  =  仅HTTPS
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFDISCSCHEMEPLY.md`
