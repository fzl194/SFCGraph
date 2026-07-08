---
id: UNC@20.15.2@MMLCommand@LST MAPGTFIXEDFC
type: MMLCommand
name: LST MAPGTFIXEDFC（查询VLR局向Map固定速率流控）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MAPGTFIXEDFC
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- Vlr Map固定速率流控
status: active
---

# LST MAPGTFIXEDFC（查询VLR局向Map固定速率流控）

## 功能

**适用NF：SMSF**

此命令用于查询VLR局向Map固定速率流控。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTNUM | GT地址 | 可选必选说明：必选参数<br>参数含义：该参数用于表示用于流控的局向SMSC的GT地址。<br>数据来源：本端规划<br>取值范围：1～16位十进制数字<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MAPGTFIXEDFC]] · VLR局向Map固定速率流控（MAPGTFIXEDFC）

## 使用实例

查询VLR局向Map固定速率流控，可以用如下命令：

```
%%LST MAPGTFIXEDFC:;%%
RETCODE = 0  操作成功  
操作结果如下 ------------              
GT地址    MO 速率门限(个/秒)      MT 速率门限(个/秒)    
1           2000                          4000                           
2           2000                          4000                          
(结果个数 = 2)  
---    结束
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MAPGTFIXEDFC.md`
