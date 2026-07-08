# 查询ULCL属性（LST ULCLPROP）

- [命令功能](#ZH-CN_CONCEPT_0216935567__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0216935567__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0216935567__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0216935567__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0216935567__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0216935567__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0216935567)

**适用NF：SMF**

该命令用于查询ULCL属性。

#### [注意事项](#ZH-CN_CONCEPT_0216935567)

如果不输入ULCL属性名称，表示查询系统中所有ULCL属性名称与DNAI对应信息。

#### [操作用户权限](#ZH-CN_CONCEPT_0216935567)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0216935567)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ULCLPROPNAME | ULCL属性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置ULCL的属性名称。该参数可供RULE命令中的“策略名称”参数引用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0216935567)

假如运营商需要查询ULCL属性名称为testulclpropname的DNAI信息：

```
LST ULCLPROP: ULCLPROPNAME="testulclpropname";
```

```

RETCODE = 0  操作成功

ULCL属性信息
-------------------------
ULCL属性名称           数据网络访问标识符 

testulclpropname       dnai1  
testulclpropname       dnai2  
testulclpropname       dnai3  
testulclpropname       dnai4  
(结果个数 = 4)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0216935567)

参见ADD ULCLPROP的参数说明。
