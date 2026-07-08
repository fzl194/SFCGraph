---
id: UNC@20.15.2@MMLCommand@LST DCNMAP
type: MMLCommand
name: LST DCNMAP（查询DCN映射关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DCNMAP
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
- DCN管理
- DCN映射关系
status: active
---

# LST DCNMAP（查询DCN映射关系）

## 功能

**适用网元：MME**

该命令用于查询DCN与UE USAGE TYPE的映射关系。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCNID | DCN ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定DCN ID。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无 |
| BGNUEUSAGETYPE | 起始UE USAGE TYPE | 可选必选说明：可选参数<br>参数含义：该参数用于指定起始UE USAGE TYPE。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无 |

## 操作的配置对象

- [DCN映射关系（DCNMAP）](configobject/UNC/20.15.2/DCNMAP.md)

## 使用实例

查询 “DCN ID” 为 “1” 的DCN与UE USAGE TYPE的映射关系：

LST DCNMAP: DCNID=1;

```
%%LST DCNMAP: DCNID=1;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
           DCN ID  =  1
起始UE USAGE TYPE  =  150
终止UE USAGE TYPE  =  180
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DCN映射关系(LST-DCNMAP)_26145830.md`
