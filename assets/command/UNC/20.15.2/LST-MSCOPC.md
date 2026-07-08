---
id: UNC@20.15.2@MMLCommand@LST MSCOPC
type: MMLCommand
name: LST MSCOPC（查询MSC信令点）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MSCOPC
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
- MSC管理
status: active
---

# LST MSCOPC（查询MSC信令点）

## 功能

**适用NF：SMSF**

该命令用于查询配置的MSC本局信令点。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPX | MSC信令点索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MSC本局信令点索引。<br>数据来源：本端规划<br>取值范围：1~2<br>默认值：无 |

## 操作的配置对象

- [MSC信令点（MSCOPC）](configobject/UNC/20.15.2/MSCOPC.md)

## 使用实例

查询已经配置的所有的MSC本局信令点。

```
%%LST MSCOPC:;%% 
RETCODE = 0  操作成功  
操作结果如下 ------------------------ 
MSC信令点索引     网络指示语  本局信令点编码   本局MSC号     是否主用信令点    
1              National Network   0x340011       8613903400110     YES          
2              National Network   0x340012       861390340012      NO           
(结果个数 = 2)  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MSC信令点(LST-MSCOPC)_78074604.md`
