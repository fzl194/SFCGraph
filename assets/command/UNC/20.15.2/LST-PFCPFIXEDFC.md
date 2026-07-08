---
id: UNC@20.15.2@MMLCommand@LST PFCPFIXEDFC
type: MMLCommand
name: LST PFCPFIXEDFC（查询指定PFCP消息类型固定速率流控信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PFCPFIXEDFC
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP流控管理
status: active
---

# LST PFCPFIXEDFC（查询指定PFCP消息类型固定速率流控信息）

## 功能

**适用NF：SMF**

该命令用于查询指定PFCP消息类型的固定速率流控信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGTYPE | 流控消息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置被流控的PFCP消息类型。<br>数据来源：全网规划<br>取值范围：<br>- HEARTBEATREQ（心跳请求）<br>- HEARTBEATRSP（心跳响应）<br>- ASSOCIATIONSETUPREQ（偶联建立请求）<br>- ASSOCIATIONSETUPRSP（偶联建立响应）<br>- ASSOCIATIONUPDATEREQ（偶联更新请求）<br>- ASSOCIATIONUPDATERSP（偶联更新响应）<br>- ASSOCIATIONRELEASEREQ（偶联释放请求）<br>- ASSOCIATIONRELEASERSP（偶联释放响应）<br>- NOTSUPPORTRSP（版本不支持响应）<br>- NODEREPORTREQ（节点上报请求）<br>- NODEREPORTRSP（节点上报响应）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PFCPFIXEDFC]] · 指定PFCP消息类型固定速率流控信息（PFCPFIXEDFC）

## 使用实例

查询所有流控消息类型流控信息，执行如下命令：

```
%%LST PFCPFIXEDFC:;%%
RETCODE = 0  操作成功

结果如下
--------
流控消息类型             固定速率流控开关  流控速率门限(个/秒)  

心跳请求                 开启              500                  
心跳响应                 开启              500                  
偶联建立请求             开启              500                  
偶联建立响应             开启              500                  
偶联更新请求             开启              500                  
偶联更新响应             开启              500                  
偶联释放请求             开启              500                  
偶联释放响应             开启              500                  
偶联释放响应             开启              500                  
版本不支持响应           开启              500       
节点上报请求             开启              500                  
节点上报响应             开启              500                                               
            
(结果个数 = 11)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PFCPFIXEDFC.md`
