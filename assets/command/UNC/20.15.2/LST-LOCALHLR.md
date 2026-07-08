---
id: UNC@20.15.2@MMLCommand@LST LOCALHLR
type: MMLCommand
name: LST LOCALHLR（查询本地HLR）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCALHLR
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- LOCALHLR管理
status: active
---

# LST LOCALHLR（查询本地HLR）

## 功能

**适用网元：SGSN、MME**

该命令用于查询本地HLR信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HLRIDX | 本地HLR索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR索引。<br>数据来源：整网规划<br>取值范围：1~256<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALHLR]] · 本地HLR（LOCALHLR）

## 使用实例

查询索引为1的本地HLR信息:

LST LOCALHLR: HLRIDX=1;

```
    %%LST LOCALHLR: HLRIDX=1;%%
    RETCODE = 0  操作成功。

    输出结果如下
    --------------
    本地HLR索引  =  1
    本地HLR号码  =  8612345678
    本地HLR名称  =  LOCALHLR1
    
    (结果个数 = 1)

    ---    END
    
```

查询所有本地HLR信息：

LST LOCALHLR;

```
%%LST LOCALHLR:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
本地HLR索引      本地HLR号码      本地HLR名称
1                8612345678       LOCALHLR1     
2                8612345679       LOCALHLR2     
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LOCALHLR.md`
