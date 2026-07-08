---
id: UNC@20.15.2@MMLCommand@LST DMAVPDICT
type: MMLCommand
name: LST DMAVPDICT（查询Diameter AVP表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DMAVPDICT
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
- 扩展调测
- 业务调测
- Diameter AVP表
status: active
---

# LST DMAVPDICT（查询Diameter AVP表）

## 功能

**适用网元：SGSN、MME**

该命令用于查询Diameter数据字典。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMAVPDICT]] · Diameter数据字典中的AVP参数（DMAVPDICT）

## 使用实例

查询Diameter数据字典：

LST DMAVPDICT:;

```
%%LST DMAVPDICT:;%%
RETCODE = 0  执行成功。

操作结果如下
-------------------------
        字典名称  =  6
        信元名称  =  129
        信元编码  =  1032
      Vendor标识  =  10415
        信元类型  =  DIAM_AVP_TYPE_UINT32
        信元标记  =  DIAM_AVP_FLAG_V_PRESENT
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Diameter-AVP表(LST-DMAVPDICT)_26145860.md`
